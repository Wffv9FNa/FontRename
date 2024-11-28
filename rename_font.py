from fontTools.ttLib import TTFont
from time import time
import sys


def rename_font(input_path, output_path, new_name):
    font = TTFont(input_path)
    for record in font["name"].names:
        if record.nameID in [1, 4, 6]:  # Family name, Full name, PostScript name
            # Handle Unicode and platform encodings
            if record.isUnicode():
                record.string = new_name.encode(
                    "utf-16-be"
                )  # Encode in UTF-16 big-endian for Unicode platforms
            else:
                # For non-Unicode platforms, attempt the record's native encoding
                try:
                    record.string = new_name.encode(record.getEncoding())
                except UnicodeEncodeError:
                    print(f"Skipping record {record} due to encoding issues.")

    # Update timestamps to the correct epoch
    current_time = int(time()) + 2082844800  # Convert UNIX timestamp to 1904 epoch
    font["head"].created = current_time  # Update 'created' timestamp
    font["head"].modified = current_time  # Update 'modified' timestamp

    font.save(output_path)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: rename_font.py <input_path> <output_path> <new_name>")
        sys.exit(1)
    rename_font(sys.argv[1], sys.argv[2], sys.argv[3])
