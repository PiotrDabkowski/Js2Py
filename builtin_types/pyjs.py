

class PyJs:
    def __setitem__(self, index, value):
        raise TypeError()
    def __getitem__(self, index):
        raise TypeError()
    def __setattr__(self, attr, val):
        raise TypeError()
    def __getattr__(self, attr):
        raise TypeError()
    def __repr__(self):
        return 'PyJsObject'