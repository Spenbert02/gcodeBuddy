# gcodeBuddy

gcodeBuddy is a python library intended to ease the process
of writing, reading, and interpreting g-code files, particularly geared towards
3D printer g-code.

## Installation

Use the package manager
[pip](https://pip.pypa.io/en/stable/) to install gcodeBuddy.

```bash
pip install gcodeBuddy
```

## Usage

```python
# imports marlin.gcode_command class
from gcodeBuddy.marlin import Command

# initializing marlin.gcode_command instance with string representing g-code line
sample_line = Command("G0 X12.3 Y45.6")

# returns "G0"
sample_line.get_command()

# returns True
sample_line.has_param("X")

# returns 12.3
sample_line.get_param("X")

sample_line.set_param("X", 32.1)
# returns 32.1
sample_line.get_param("X")
```

## Supported G-code Flavors

Marlin

## Contributions

Pull requests are more than welcome. For most cases, open
an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
