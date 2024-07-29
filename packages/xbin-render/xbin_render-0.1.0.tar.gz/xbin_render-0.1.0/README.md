# xbin_render

Render [XBin](https://en.wikipedia.org/wiki/XBin) (`.XB`) images to PNG or to terminal.
XBin files are similar to ANSI-art images, as they consist of characters on a background, with 16 colors.

## Install

    pipx install xbin_render

## Usage

Show on terminal

    xbin_render file.xbin

Convert to PNG

    xbin_render file.xbin --output-image file.png

## Format

The spec is at https://www.acid.org/images/0896/XBIN.TXT but it's incomplete as it relies on knowledge on VGA, etc.

## Limitations

The format supports custom fonts, which cannot be rendered easily on a terminal (converting to ressembling characters could be done though).
Rendering to PNG without a custom font is not implemented yet.

## What about `.ANS`/`.ASC` files?

In a color-capable terminal: `iconv -f cp437 MYFILE.ANS`

## License

xbin_render is licensed under the [WTFPLv2](COPYING.wtfpl).
