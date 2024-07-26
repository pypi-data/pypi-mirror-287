import functools
import re
from abc import ABCMeta


def restrict_type(type=None):
    type_ = type or str

    def decorator(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            _, value, *_ = args
            if isinstance(value, type_):
                return f(*args, **kwargs)
            return value

        return wrapper

    return decorator


class Loop:
    """
    Loop over a list of values and apply a function to each of them.
    """

    def __init__(self, function):
        self.function = function

    def __call__(self, values):
        return [
            self.function(value)
            for value in values
        ]


class Compose:
    """
    Compose a list of functions into one function.
    """

    def __init__(self, *functions):
        self.functions = functions

    def __call__(self, value):
        for func in self.functions:
            try:
                value = func(value)
            except Exception as e:
                raise ValueError(
                    "Error in Compose with "
                    "%s value=%r error='%s: %s'"
                    % (str(func), value, type(e).__name__, str(e))
                ) from e
        return value


class Processor(metaclass=ABCMeta):

    def __call__(self, *args, **kwargs):
        raise NotImplementedError

    def __str__(self):
        return f"`\x1B[3m{self.__class__.__name__}\x1B[0m`"


class Identity(Processor):
    """
    The simplest processor, which doesn't do anything. It returns the original
    """

    def __call__(self, value):
        return value


class First(Processor):
    """
    get first non-null/non-empty value from the values received,

    >>> proc = First()
    >>> proc(['', 'one', 'two', 'three'])
    'one'
    """

    def __call__(self, values):
        for value in values:
            if value and value != "":
                return value


class Join(Processor):
    """ Concatenate any list of strings. """

    def __init__(self, join_string=''):
        self.join_string = join_string

    def __call__(self, values):
        return self.join_string.join(values)


class Middle(Processor):
    """ get middle text from value """

    def __init__(self, left: str, right: str, flags=0):
        self.left = left
        self.right = right
        self.pattern = re.compile(fr"{left}(.*?){right}", flags)

    @restrict_type(str)
    def __call__(self, value):
        obj = self.pattern.search(value)
        return None if obj is None else obj.group(1)


class Format(Processor):
    """ format value with args """

    def __init__(self, fmt: str):
        self.fmt = fmt

    @restrict_type(str)
    def __call__(self, value):
        return self.fmt.format(value)


class Strip(Processor):
    """ strip value """

    @restrict_type(str)
    def __call__(self, value):
        return value.strip()


class Upper(Processor):
    """ upper value """

    @restrict_type(str)
    def __call__(self, value):
        return value.upper()


class Filter(Processor):
    """ filter value """

    def __init__(self, function):
        self.function = function

    def __call__(self, value):
        return list(filter(self.function, value))


class To(Processor):
    """ convert value to type """

    def __init__(self, type):
        self.type = type

    def __call__(self, value):
        return self.type(value)


__all__ = [
    'Identity',
    'Compose',
    'Loop',
    'First',
    'Join',
    'Middle',
    'Format',
    'Upper',
    'Strip',
    'Filter',
    'To',
]
