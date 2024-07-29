"""
将字符串转换为带颜色的字符串

参考:
  - https://en.wikipedia.org/wiki/ANSI_escape_code#Colors

使用:

```python
Color('Hello World!').red()

Color('Hello World!').bold().italic().underline().fg_red()
```

Author: Jared Zhang
Email: zyjared@outlook.com

Github: https://github.com/zyjared/kit-python
"""

from typing import Callable, Self

COLORS = {
    'black': 30,
    'red': 31,
    'green': 32,
    'yellow': 33,
    'blue': 34,
    'magenta': 35,
    'cyan': 36,
    'white': 37,
    'bright_black': 90,
    'bright_red': 91,
    'bright_green': 92,
    'bright_yellow': 93,
    'bright_blue': 94,
    'bright_magenta': 95,
    'bright_cyan': 96,
    'bright_white': 97,
}


class Text:
    def __init__(self, value):
        # [bold, italic, underline, fg, bg]
        self._sequence = [None for _ in range(5)]
        self._value = value or ''

    def bold(self):
        self._sequence[0] = 1
        return self

    def italic(self):
        self._sequence[1] = 3
        return self

    def underline(self):
        self._sequence[2] = 4
        return self

    def _fg(self, color: str):
        self._sequence[3] = COLORS[color]
        return self

    def _bg(self, color: str):
        self._sequence[4] = COLORS[color] + 10
        return self

    def _serialize(self):
        sequence = [str(x) for x in self._sequence if x is not None]

        if len(sequence) == 0:
            return self._value

        attrs = ';'.join(sequence)
        return f'\033[{attrs}m{self._value}\033[0m'

    def __str__(self):
        return self._serialize()

    def to_str(self):
        return self._serialize()

    # fg

    black: Callable[[], Self]
    red: Callable[[], Self]
    green: Callable[[], Self]
    yellow: Callable[[], Self]
    blue: Callable[[], Self]
    magenta: Callable[[], Self]
    cyan: Callable[[], Self]
    white: Callable[[], Self]
    bright_black: Callable[[], Self]
    bright_red: Callable[[], Self]
    bright_green: Callable[[], Self]
    bright_yellow: Callable[[], Self]
    bright_blue: Callable[[], Self]
    bright_magenta: Callable[[], Self]
    bright_cyan: Callable[[], Self]
    bright_white: Callable[[], Self]

    # bg

    bg_black: Callable[[], Self]
    bg_red: Callable[[], Self]
    bg_green: Callable[[], Self]
    bg_yellow: Callable[[], Self]
    bg_blue: Callable[[], Self]
    bg_magenta: Callable[[], Self]
    bg_cyan: Callable[[], Self]
    bg_white: Callable[[], Self]
    bg_bright_black: Callable[[], Self]
    bg_bright_red: Callable[[], Self]
    bg_bright_green: Callable[[], Self]
    bg_bright_yellow: Callable[[], Self]
    bg_bright_blue: Callable[[], Self]
    bg_bright_magenta: Callable[[], Self]
    bg_bright_cyan: Callable[[], Self]
    bg_bright_white: Callable[[], Self]


for color in COLORS:
    setattr(Text, color, lambda self, c=color: self._fg(c))
    setattr(Text, f'bg_{color}', lambda self, c=color: self._bg(c))


class Color(Text):
    def __init__(self, value):
        super().__init__(value)


def main():
    types = ['bold', 'italic', 'underline', 'bg']
    for t in types:
        cato = str(Color(t).red().bold())
        print(f'{cato:<20}')
        for color in COLORS:
            text = getattr(Text('Hello World!'), color)()
            if t == 'bg':
                text = getattr(text, f'bg_{color}')()
            else:
                text = getattr(text, t)()

            c = str(Color(color).green())
            print(f'\t{c:<30} : {text}')


if __name__ == '__main__':
    main()
