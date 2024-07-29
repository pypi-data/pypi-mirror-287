# zyjared-color

## Reference

- [wiki: ANSI escape code](https://en.wikipedia.org/wiki/ANSI_escape_code#Colors)

## Usage

```python
from zyjared.color import Color

Color('Hello World!').red()

Color('Hello World!').bold().italic().underline().fg_red()
```