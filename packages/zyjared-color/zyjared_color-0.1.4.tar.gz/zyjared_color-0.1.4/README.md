# zyjared-color

## Reference

- [wiki: ANSI escape code](https://en.wikipedia.org/wiki/ANSI_escape_code#Colors)

## Installation

```sh
pip install zyjared-color
```

## Usage

```python
from zyjared_color import Color

Color('Hello World!').red()

Color('Hello World!').bold().italic().underline().fg_red()
```