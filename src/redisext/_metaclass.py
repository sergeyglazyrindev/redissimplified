from functools import wraps


def wrapped_redisext_method(name):
    def wrapper(cls, *args):
        if hasattr(cls, 'KEY'):
            args = list(args)
            args.insert(0, getattr(cls, 'KEY'))
            args = tuple(args)
        _redis = cls._redis()
        return getattr(_redis, name)(*args)
    return classmethod(wrapper)


class RedisKeyHandler(type):

    def __new__(cls, name, bases, attrs):

        for command in attrs.get('allowed_commands', ()):
            if command in attrs:
                continue
            attrs[command] = wrapped_redisext_method(command)
        if attrs.get('KEY'):
            def wrapped_method(func):
                @wraps(func)
                def wrapper(cls, *args):
                    return func(cls, attrs.get('KEY'), *args)
                return classmethod(wrapper)
            for attrname, attrvalue in attrs.items():
                if attrname.startswith('_'):
                    continue
                if not hasattr(attrvalue, '__call__'):
                    continue
                attrs[attrname] = wrapped_method(attrvalue)
        return super(RedisKeyHandler, cls).__new__(cls, name, bases, attrs)
