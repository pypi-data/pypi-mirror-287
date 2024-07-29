#!/usr/bin/env python3
# SPDX-License-Identifier: WTFPL

import argparse
from dataclasses import dataclass
import enum
import struct


__version__ = "0.1.0"


DEFAULT_PALETTE = [
    (0, 0, 0),
    (0, 0, 170),
    (0, 170, 0),
    (0, 170, 170),
    (170, 0, 0),
    (170, 0, 170),
    (170, 85, 0),
    (170, 170, 170),
    (85, 85, 85),
    (85, 85, 255),
    (85, 255, 85),
    (85, 255, 255),
    (255, 85, 85),
    (255, 85, 255),
    (255, 255, 85),
    (255, 255, 255),
]


class HeaderFlag(enum.IntFlag):
    Palette = 1 << 0
    Font = 1 << 1
    Compress = 1 << 2
    NonBlink = 1 << 3
    Char512 = 1 << 4


class CompressFlag(enum.IntFlag):
    CharCompress = 1 << 6
    AttrCompress = 1 << 7
    CompressMask = CharCompress | AttrCompress
    SizeMask = (1 << 6) - 1

    @property
    def compressed(self):
        return self & self.CompressMask

    @property
    def counter(self):
        return int(self & self.SizeMask) + 1


class AttrFlag(enum.IntFlag):
    FgBlue = 1 << 0
    FgGreen = 1 << 1
    FgRed = 1 << 2
    FgIntensity = Plane512 = 1 << 3
    BgBlue = 1 << 4
    BgGreen = 1 << 5
    BgRed = 1 << 6
    BgIntensity = Blink = 1 << 7
    FgMask = FgBlue | FgRed | FgGreen | FgIntensity
    BgMask = BgBlue | BgRed | BgGreen | BgIntensity

    @property
    def fg(self):
        return int(self & self.FgMask)

    @property
    def bg(self):
        return int(self & self.BgMask) >> 4


class Struct:
    @classmethod
    def build_from(cls, buffer, offset=0):
        fields = struct.unpack_from(cls.FORMAT, buffer, offset)
        return cls(*fields)

    @classmethod
    def read_from(cls, fp):
        size = struct.calcsize(cls.FORMAT)
        buffer = fp.read(size)
        fields = struct.unpack(cls.FORMAT, buffer)
        return cls(*fields)


@dataclass
class Header(Struct):
    FORMAT = "<5s2HBB"

    magic: bytes
    width: int
    height: int
    fontsize: int
    flags: int

    def __post_init__(self):
        assert self.magic == b"XBIN\x1a"
        self.flags = HeaderFlag(self.flags)


@dataclass
class Palette(Struct):
    FORMAT = "48B"

    values: list[int]

    def __init__(self, *values):
        # from the spec, values are in the range 0-63, so we `* 4` to be < 256
        self.values = [
            (values[i] * 4, values[i+1] * 4, values[i+2] * 4)
            for i in range(0, 48, 3)
        ]


@dataclass
class File:
    header: Header | None = None
    palette: Palette | None = None
    font: None = None
    image: bytes | None = None

    def read_font(self, fp):
        fontnb = 256
        if self.header.flags & HeaderFlag.Char512:
            fontnb = 512

        result = []
        for charid in range(fontnb):
            result.append(fp.read(self.header.fontsize))
        self.font = result

    def read_data(self, fp):
        if self.header.flags & HeaderFlag.Compress:
            self.read_compressed(fp)
        else:
            self.read_uncompressed(fp)

    def read_uncompressed(self, fp):
        result = []
        for _ in range(self.header.height):
            result.append(fp.read(self.header.width * 2))
        self.image = result

    def read_compressed_row(self, fp):
        result = bytearray()
        while len(result) < self.header.width * 2:
            compression = CompressFlag(fp.read(1))

            if not compression.compressed:
                buffer = fp.read(compression.count * 2)
                result += buffer
            else:
                common = fp.read(1)
                different = fp.read(compression.count)
                for d in different:
                    if compression & compression.CharCompress:
                        result += common + different.to_bytes()
                    else:
                        result += different.to_bytes() + common
        return result

    def read_compressed(self, fp):
        # this part is not really tested
        result = []
        for _ in range(self.header.height):
            result.append(self.read_compressed_row(fp))
        self.image = result

    def get_chr(self, buf):
        plane = 0
        if self.header.flags & HeaderFlag.Char512:
            plane = bool(buf[1] & AttrFlag.Plane512)
        return buf[0] + plane * 256

    def get_fg(self, buf):
        attr = AttrFlag(buf[1])
        if self.palette:
            return self.palette.values[attr.fg]
        return attr.fg

    def get_bg(self, buf):
        attr = AttrFlag(buf[1])
        if self.palette:
            return self.palette.values[attr.bg]
        return attr.bg


def print_file(f):
    if f.header.flags & HeaderFlag.Char512:
        raise NotImplementedError("512 chars mode is not implemented for text mode")

    for row in f.image:
        for offset in range(0, len(row), 2):
            char = f.get_chr(row[offset:offset+2]).to_bytes().decode("cp437")
            char = "█"
            fg = f.get_fg(row[offset:offset+2])
            bg = f.get_bg(row[offset:offset+2])
            if f.palette:
                print(
                    f"\x1b[48;2;{bg[0]};{bg[1]};{bg[2]}m{char}"
                    + f"\x1b[38;2;{fg[0]};{fg[1]};{fg[2]}m",
                    end=""
                )
            else:
                print(f"\x1b[38;5;{fg}m\x1b[48;5;{bg}m{char}", end="")
        print("\x1b[0m")


def _build_font(f, data):
    from PIL import Image

    im = Image.new("1", (8, f.header.fontsize))
    for row in range(f.header.fontsize):
        sub = data[row]
        for col in range(8):
            # print(int(bool(sub & (1 << col))), end="")
            im.putpixel((7 - col, row), int(bool(sub & (1 << col))))

        # print()
    return im


def render_file(f: File, output_filename: str):
    from PIL import Image

    if not f.font:
        raise NotImplementedError("default font is not implemented in image mode")

    patterns = [
        _build_font(f, data) for data in f.font
    ]

    im = Image.new(
        "RGB", (f.header.width * 8, f.header.height * f.header.fontsize)
    )

    for nrow, row in enumerate(f.image):
        for ncol, offset in enumerate(range(0, len(row), 2)):
            char = f.get_chr(row[offset:offset+2])
            pattern = patterns[char]

            fg = f.get_fg(row[offset:offset+2])
            bg = f.get_bg(row[offset:offset+2])
            if not f.palette:
                fg = DEFAULT_PALETTE[fg]
                bg = DEFAULT_PALETTE[bg]
            rect = (
                ncol * pattern.width,
                nrow * pattern.height,
                (ncol + 1) * pattern.width,
                (nrow + 1) * pattern.height,
            )
            im.paste(bg, rect)
            im.paste(fg, rect, mask=pattern)

    im.save(output_filename, "PNG")

# TODO blink mode


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output-image",
        metavar="FILE",
        help="write image to FILE as PNG",
    )
    parser.add_argument("input", help="input XBin file")
    args = parser.parse_args()

    xbin = File()
    with open(args.input, "rb") as fp:
        xbin.header = Header.read_from(fp)
        if xbin.header.flags & HeaderFlag.Palette:
            xbin.palette = Palette.read_from(fp)
        if xbin.header.flags & HeaderFlag.Font:
            xbin.read_font(fp)
        xbin.read_data(fp)

    if args.output_image:
        render_file(xbin, args.output_image)
    else:
        print_file(xbin)


if __name__ == "__main__":
    main()
