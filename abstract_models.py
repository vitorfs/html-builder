from utils import extract_attrs, pretty_name

class AbstractTag(object):

    def __str__(self):
        return '<{0}{1}>{2}</{3}>'.format(
            self._tag_name, 
            extract_attrs(self._join_attrs()),
            self._text, 
            self._tag_name
            )
    
    def __init__(self, text=''):
        self._id = ''
        self._class = ''
        self._attrs = {}
        self._text = text
        self._tag_name = self.__class__.__name__.lower()

    def id(self, value):
        self._id = value
        return self

    def css_class(self, value):
        self._class += (' ' + value).strip()
        return self

    def attrs(self, values):
        self._attrs = dict(self._attrs.items() + values.items())
        return self

    def text(self, value):
        self._text = str(value)
        return self

    def append(self, value):
        self._text = str(self._text) + str(value)
        return self

    def prepend(self, value):
        self._text = str(value) + str(self._text)
        return self

    def _join_attrs(self):
        if self._id:
            self._attrs['id'] = self._id
        if self._class:
            if 'class' in self._attrs.keys():
                self._attrs['class'] = self._attrs['class'] + ' ' + self._class
            else: 
                self._attrs['class'] = self._class
        return self._attrs

class AbstractFormTag(AbstractTag):
    
    def __init__(self, text=''):
        self._type = ''
        self._value = ''
        super(AbstractFormTag, self).__init__(text)

    def type(self, value):
        self._type = value
        return self

    def _join_attrs(self):
        if self._type:
            self._attrs['type'] = self._type
        if self._value:
            self.attrs['value'] = self._value
        return super(AbstractFormTag, self)._join_attrs()