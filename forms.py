from abstract_models import AbstractFormTag
from utils import extract_attrs

class Input(AbstractFormTag):
    def __str__(self):
        return '<{0}{1}>'.format(
            self._tag_name, 
            extract_attrs(self._join_attrs())
            )

class Button(AbstractFormTag):
    pass