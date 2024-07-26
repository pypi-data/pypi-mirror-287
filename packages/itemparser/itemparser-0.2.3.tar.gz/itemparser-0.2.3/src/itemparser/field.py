from functools import partial

from parsel import Selector as _Selector


class _UNSET:
    pass


class Field:
    selector_class = None

    def __init__(self, expression: str, **ctx):
        self.expression = expression
        self.ctx = ctx
        self.processor = self.ctx.setdefault('processor', _UNSET)
        self._error = None

    def __str__(self):
        class_name = self.__class__.__name__
        return (
            class_name
            if not class_name.endswith('Field')
            else class_name[:-5]
        ).lower()

    @property
    def error(self):
        return self._error

    @error.setter
    def error(self, value):
        self._error = value

    def has_processor(self):
        return self.processor is not _UNSET

    def handle_process(self, value):
        if self.processor is None:
            return value
        try:
            return self.processor(value)  # noqa
        except Exception as e:
            self.error = e


class _Html(Field):
    """ base html field """
    selector_class = partial(_Selector, type="html")


class XpathField(_Html):
    """ define `xpath` field """


class CssField(_Html):
    """ define `css` field"""


class ReField(_Html):
    """ define `re` field """


class JsonField(Field):
    """ define `json` field """
    selector_class = partial(_Selector, type="json")

    def __str__(self):
        return 'jmespath'


class TextField(Field):
    selector_class = partial(_Selector, type="text")
