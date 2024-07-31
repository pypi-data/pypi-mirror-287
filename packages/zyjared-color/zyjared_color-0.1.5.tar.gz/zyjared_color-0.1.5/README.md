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

a = Color.red('Hello World!')
print(a)

b = Color.bold('Hello World!').italic().underline().bg_blue()
print(b)

c = Color.red('Hello') + ' ' + Color.blue('World') + '!!!'
print(c)

d = Color('extend styles').extend(a)
print(d)

e = b.clean().red()
print(e)
```


## Styles

- `Color.bold()`
- `Color.italic()`
- `Color.underline()`
- `Color.dim()`
- `Color.through()`
- `Color.reverse()`
- `Color.blink()`
- `Color.blink_fast()`
- `Color.hidden()`

### foreground

- `Color.black()`
- `Color.red()`
- `Color.green()`
- `Color.yellow()`
- `Color.blue()`
- `Color.magenta()`
- `Color.cyan()`
- `Color.white()`
- `Color.bright_black()`
- `Color.bright_red()`
- `Color.bright_green()`
- `Color.bright_yellow()`
- `Color.bright_blue()`
- `Color.bright_magenta()`
- `Color.bright_cyan()`
- `Color.bright_white()`

### background

- `Color.bg_black()`
- `Color.bg_red()`
- `Color.bg_green()`
- `Color.bg_yellow()`
- `Color.bg_blue()`
- `Color.bg_magenta()`
- `Color.bg_cyan()`
- `Color.bg_white()`
- `Color.bg_bright_black()`
- `Color.bg_bright_red()`
- `Color.bg_bright_green()`
- `Color.bg_bright_yellow()`
- `Color.bg_bright_blue()`
- `Color.bg_bright_magenta()`
- `Color.bg_bright_cyan()`
- `Color.bg_bright_white()`
