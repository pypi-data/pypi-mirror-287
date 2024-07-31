from typing import Literal, Self, Type
from .constant import COLORS, COLORS_BG, STYLES, STYLES_LENGTH


class StyleMeta(type):
    def __new__(cls: Type[Self], name: str, bases: tuple, dct: dict) -> Type[Self]:
        new_class = super().__new__(cls, name, bases, dct)
        cls._setup(new_class)
        return new_class

    @staticmethod
    def _setup(cls):
        # Dynamic create style methods
        for i in range(2, STYLES_LENGTH):
            setattr(cls, STYLES[i][0],
                    StyleMeta._gen_style_method(STYLES[i][1], i))

        # Dynamic create color methods
        for color in COLORS.keys():
            setattr(cls, color, StyleMeta._gen_color_method(COLORS[color], 0))
        for color in COLORS_BG.keys():
            setattr(cls, color, StyleMeta._gen_color_method(COLORS_BG[color], 1))

    @staticmethod
    def _gen_style_method(code: int, index: int):
        def wrapper(self):
            # Index: see .constant.STYLES
            self._seq[index] = code
            return self
        return wrapper

    @staticmethod
    def _gen_color_method(code: int,index: Literal[0, 1]):
        def wrapper(self):
            self._seq[index] = code
            return self
        return wrapper


class Style(metaclass=StyleMeta):

    def __init__(self, text: str):
        # Order and length: see .constant.STYLES
        self._seq = bytearray(STYLES_LENGTH)
        self.text = None
        if isinstance(text, Style):
            self.extend(text)
        else:
            self.text = text

    def extend(self, src: Self):
        for i in range(STYLES_LENGTH):
            if src._seq[i]:
                self._seq[i] = src._seq[i]
        return self

    def clean(self):
        self._seq = bytearray(STYLES_LENGTH)
        return self

    @staticmethod
    def _to_bytes(text):
        if isinstance(text, str):
            return text.encode()
        elif isinstance(text, (bytes, bytearray)):
            return text
        else:
            return f'{text}'.encode()

    def _compose_styles(self):
        # start
        ba = bytearray(b'\033[')
        ba.extend(b';'.join(str(code).encode() for code in self._seq if code))
        ba.extend(b'm')

        # text
        ba.extend(Style._to_bytes(self.text))

        # end
        ba.extend(b'\033[0m')

        return ba

    def to_bytearray(self):
        if not self.text:
            return bytearray()
        elif not any(self._seq):
            ba = Style._to_bytes(self.text)
            if isinstance(ba, bytearray):
                return ba
            else:
                return bytearray(ba)
        else:
            return self._compose_styles()

    def to_str(self):
        if not self.text:
            return ''
        elif not any(self._seq):
            return self.text
        else:
            return self._compose_styles().decode()

    def __str__(self):
        return self.to_str()

    def __format__(self, format_spec: str):
        return f'{self.to_str():{format_spec}}'

    def __add__(self, other):
        if isinstance(other, Style):
            ba = self.to_bytearray()
            ba.extend(other.to_bytearray())
            return ba.decode()
        else:
            return f'{self.to_str()}{other}'

    def __radd__(self, other):
        if isinstance(other, Style):
            ba = other.to_bytearray()
            ba.extend(self.to_bytearray())
            return ba.decode()
        else:
            return f'{other}{self.to_str()}'
