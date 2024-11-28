# Font Renamer

A simple Python script to rename fonts by modifying their internal name records. This is useful for changing the family name, full name, or PostScript name of a font file.

## Features

- Rename font's internal name records (Family name, Full name, PostScript name)
- Update font creation and modification timestamps to the current time

## Requirements

- Python 3.x
- [fontTools](https://github.com/fonttools/fonttools)

## Installation

Install the required dependencies using pip:

```bash
pip install fonttools
````

Usage
-----

```bash
python rename_font.py <input_path> <output_path> <new_name>
```

*   `<input_path>`: Path to the input font file (e.g., `input.ttf`)
*   `<output_path>`: Path to save the renamed font file (e.g., `output.ttf`)
*   `<new_name>`: The new name to assign to the font's name records

### Example

```bash
python rename_font.py original_font.ttf renamed_font.ttf "New Font Name"
```

License
-------

This project is licensed under the MIT License.

Contributing
------------

Contributions are welcome! Please open an issue or submit a pull request.

Acknowledgments
---------------

*   [fontTools](https://github.com/fonttools/fonttools) library for font manipulation


---

### `LICENSE`

```text
MIT License

Copyright (c) 2024 Wffv9FNa

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
````