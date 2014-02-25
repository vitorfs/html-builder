from forms import Input, Button
from typography import A, P, Strong

print P() \
    .append(A('google').href('google.com')) \
    .append(Button('(remover)').css_class('btn btn-small'))