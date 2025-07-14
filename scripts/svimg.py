#!/usr/bin/env python
"""
Small utility to:

1. locate a pasted in `image.png`
2. mv it to `images` dir and rename it to the specified name
3. find-replace any references to it in `presentation.md`

"""
import os
import sys

from pathlib import Path


def main():
    if len(sys.argv) != 2:
        print(
            "Requires exactly one argument, which is the new name of the image (minus extension).",
            file=sys.stderr,
        )
        sys.exit(1)

    new_name = sys.argv[1]

    cwd = Path(os.getcwd())

    image = cwd / "image.png"
    if image.exists():
        print(f"{image} exists", file=sys.stderr)
    else:
        print(f"{image} does not exist", file=sys.stderr)
        sys.exit(1)

    # mv the image and rename it
    images = cwd / "images"
    images.mkdir(exist_ok=True)
    new_name = images / f"{new_name}.png"
    os.rename(image, new_name)
    print(f"Moved {image} to {new_name}", file=sys.stderr)

    # Update name in presentation.md
    with open(cwd / "presentation.md", "r") as fh:
        filedata = fh.read()

    filedata = filedata.replace("image.png", str(new_name.relative_to(cwd)))

    with open(cwd / "presentation.md", "w") as fh:
        fh.write(filedata)

    print("Updated name in presentation.md")


if __name__ == "__main__":
    main()
