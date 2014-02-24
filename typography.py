from abstract_models import AbstractTag

class H1(AbstractTag):
    pass

class H2(AbstractTag):
    pass

class H3(AbstractTag):
    pass

class H4(AbstractTag):
    pass

class H5(AbstractTag):
    pass

class H6(AbstractTag):
    pass

class P(AbstractTag):
    pass

class A(AbstractTag):

    def href(self, value):
        self._href = value
        return self

    def target(self, value):
        self._target = value
        return self

    def _join_attrs(self):
        if self._href:
            self._attrs['href'] = self._href
        if self._target:
            self._attrs['target'] = self._target
        return super(A, self)._join_attrs()

class Strong(AbstractTag):
    pass

class B(AbstractTag):
    pass

class Em(AbstractTag):
    pass

class I(AbstractTag):
    pass

class U(AbstractTag):
    pass