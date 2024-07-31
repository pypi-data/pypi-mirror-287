from parsel import SelectorList

from itemparser import field
from itemparser.field import Field, TextField
from itemparser.processor import Identity


class ParserMetaclass(type):

    def __new__(mcs, name, bases, attrs):
        fields = [(field_name, attrs.pop(field_name))
                  for field_name, obj in list(attrs.items())
                  if isinstance(obj, Field)]
        attrs['_fields'] = fields
        new_class = super().__new__(mcs, name, bases, attrs)
        new_class._meta = getattr(new_class, "Meta", None)
        return new_class


class BaseParser:
    default_data_class = dict
    default_processor = Identity()
    raise_exception = True

    def __init__(self, data=None):
        self.data = data or self.default_data_class()
        self._values = {}

    @classmethod
    def from_config(cls, config: dict):
        for key, value in config.items():
            for f in value:
                cls._fields.append(
                    (f.get('field_name'),
                     getattr(field, f.get('selector').title())(f.get('expression')))
                )
        return cls

    def parse(self, field_name, f: Field):
        value = self._get_value(f)

        processed_value = self._get_process_value(value, f)

        return self._add_value(field_name, processed_value)

    def _get_process_value(self, value, f: Field):
        if not f.has_processor():
            processed_value = self.default_processor(value)
        else:
            processed_value = f.handle_process(value)
        if f.error and self.raise_exception:
            raise f.error
        return processed_value

    def _get_value(self, f: Field):
        if isinstance(f, TextField):
            return f.expression
        parsed = getattr(f.selector_class(self.data), str(f))(f.expression)
        if isinstance(parsed, SelectorList):
            return parsed.getall()
        return parsed

    def _add_value(self, field_name, value):
        self._values.setdefault(field_name, value)

    @property
    def result(self):
        for field_name, field_obj in self._fields:
            self.parse(field_name, field_obj)
        return self._values


class Parser(BaseParser, metaclass=ParserMetaclass):
    pass


class ListParser(Parser):
    def __init__(self, data = None, fill_value = None):
        super().__init__(data)
        self._values = []
        self.fill_value = fill_value

    def parse(self):
        lists = [self._get_value(f) for _, f in self._fields]
        max_length = max(len(lst) for lst in lists)

        padded_lists = [
            list(lst) + [self.fill_value] * (max_length - len(lst))
            for lst in lists
        ]
        for items in zip(*padded_lists):
            value = dict(zip([field_name for field_name, f in self._fields], items))

            for field_name, f in self._fields:
                field_value = value.get(field_name, None)
                if field_value:
                    value[field_name] = self._get_process_value(field_value, f)

            self._add_values(value)

    def _add_values(self, values):
        self._values.append(values)

    @property
    def result(self):
        self.parse()
        return self._values