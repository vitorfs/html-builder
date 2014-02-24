def extract_attrs(attrs):
    str_attrs = []
    if attrs:
        for key in attrs.keys():
            str_attrs.append('{0}="{1}"'.format(key, attrs[key]))
    if len(str_attrs) > 0:
        return ' ' + ' '.join(str_attrs)
    else:
        return ''

def pretty_name(name):
    if not name:
        return ''
    return name.replace('_', ' ').capitalize()