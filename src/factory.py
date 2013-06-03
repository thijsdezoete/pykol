class KolFactory(object):
    def __new__(klass, name, *args, **kwargs):
        _base = 'kol'
        _module_name = 'request'

        if 'Database' in name:
            _module_name = 'database'

        _full_mod = '.'.join([_base, _module_name, name])
        _func_name = [name] if args or kwargs else name

        _my_mod = __import__(_full_mod, globals(), locals(), _func_name, -1)
        if not args and not kwargs:
            return _my_mod
        else:
            return getattr(_my_mod, name)(*args, **kwargs)

    def __init__(self, *args, **kwargs):
        """ KolFactory by Thijs de Zoete """
        pass
