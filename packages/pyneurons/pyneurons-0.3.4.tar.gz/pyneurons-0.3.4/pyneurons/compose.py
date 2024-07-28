def compose(name, cls, function):
    def __call__(self, x):
        return function(cls.__call__(self, x))

    return type(name, (cls,), {"__call__": __call__})
