from abstract_models import AbstractTag

class ListBuilder(AbstractTag):
    pass

class TableBuilder(AbstractTag):

    def __init__(self):
        self._header = []
        self._body = []
        self._data = []
        super(Table, self).__init__()

    def header(self, *args):
        for arg in args:
            if type(arg) is list:
                for attr in arg:
                    self._header.append(attr)
            else:
                self._header.append(arg)
        return self

    def data_attrs(self, *args):
        for arg in args:
            if type(arg) is list:
                for attr in arg:
                    self._body.append(attr)
            else:
                self._body.append(arg)
        return self

    def data(self, values):
        self._data = values
        return self

    def _extract_dict_columns(self, values):
        for key in values.keys():
            self._header.append(key)
            self._body.append(values[key])

    def _extract_list_columns(self, values):
        for value in values:
            self._header.append(pretty_name(value))
            self._body.append(value)

    def _extract_str_column(self, value):
        self._header.append(pretty_name(value))
        self._body.append(value)

    def columns(self, *values):
        for value in values:
            if type(value) is str:
                self._extract_str_column(value)
            elif type(value) is dict:
                self._extract_dict_columns(value)
                pass
            elif type(value) is list:
                self._extract_list_columns(value)
        return self

    def build(self):
        html = '<table%s>' % extract_attrs(self._join_attrs())

        if self._header:
            html += '<thead><tr>'
            for col in self._header:
                html += '<th>%s</th>' % col
            html += '</tr></thead>'

        if self._body:
            html += '<tbody>'
            for element in self._data:
                html += '<tr oid="%s">' % element.id
                for col in self._body:
                    html += '<td>%s</td>' % getattr(element, col)
                html += '</tr>'
            html += '</tbody>'

        html += '</table>'

        return html