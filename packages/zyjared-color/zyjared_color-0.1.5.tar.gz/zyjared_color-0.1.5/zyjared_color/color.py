from functools import partial
from typing import Self, Type
from .style import Style
from .constant import COLORS, COLORS_BG, STYLES


class ColorMeta(type):

    def __new__(cls: Type[Self], name: str, bases: tuple, dct: dict) -> Type[Self]:
        new_class = super().__new__(cls, name, bases, dct)
        cls._setup(new_class)
        return new_class

    @staticmethod
    def _setup(cls):
        for attr in [
            *[i[0] for i in STYLES],
            *[k for k in COLORS.keys()],
            *[k for k in COLORS_BG.keys()]
        ]:
            setattr(cls, attr, staticmethod(partial(ColorMeta._gen_method(attr))))

    @staticmethod
    def _gen_method(attr: str):
        def _static_method(text: str):
            return getattr(Style(text), attr)()
        return _static_method


class Color(metaclass=ColorMeta):
    def __new__(cls: Type[Self], text: str) -> Style:
        return Style(text)
