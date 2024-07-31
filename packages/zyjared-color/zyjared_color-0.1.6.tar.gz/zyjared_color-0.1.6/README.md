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

f = Color.extend(e)
```

## Color

The `Color` class provides static methods that return instances of the `Style` class.

### `Style` class

The static methods of the `Color` class are designed to create and return instances of the `Style` class. Each method in the `Color` class returns a `Style` instance, which can then be used for further manipulation.

- `Color( text: str ) -> Instance[Style]`
- `Style( text: str | None = ... ) -> Instance[Style]`

### methods

- `Color.extend( style: Style )`
- `Color.clean( style: Style )`

### styles

- `Color.bold( text: str )`
- `Color.italic( text: str )`
- `Color.underline( text: str )`
- `Color.dim( text: str )`
- `Color.through( text: str )`
- `Color.reverse( text: str )`
- `Color.blink( text: str )`
- `Color.blink_fast( text: str )`
- `Color.hidden( text: str )`

### foreground

- `Color.black( text: str )`
- `Color.red( text: str )`
- `Color.green( text: str )`
- `Color.yellow( text: str )`
- `Color.blue( text: str )`
- `Color.magenta( text: str )`
- `Color.cyan( text: str )`
- `Color.white( text: str )`
- `Color.bright_black( text: str )`
- `Color.bright_red( text: str )`
- `Color.bright_green( text: str )`
- `Color.bright_yellow( text: str )`
- `Color.bright_blue( text: str )`
- `Color.bright_magenta( text: str )`
- `Color.bright_cyan( text: str )`
- `Color.bright_white( text: str )`

### background

- `Color.bg_black( text: str )`
- `Color.bg_red( text: str )`
- `Color.bg_green( text: str )`
- `Color.bg_yellow( text: str )`
- `Color.bg_blue( text: str )`
- `Color.bg_magenta( text: str )`
- `Color.bg_cyan( text: str )`
- `Color.bg_white( text: str )`
- `Color.bg_bright_black( text: str )`
- `Color.bg_bright_red( text: str )`
- `Color.bg_bright_green( text: str )`
- `Color.bg_bright_yellow( text: str )`
- `Color.bg_bright_blue( text: str )`
- `Color.bg_bright_magenta( text: str )`
- `Color.bg_bright_cyan( text: str )`
- `Color.bg_bright_white( text: str )`
