from functools import wraps


def wrapped_redisext_method(name):
    def wrapper(cls, *args, **kwargs):
        _redis = cls._redis()
        return getattr(_redis, name)(*args, **kwargs)
    return wrapper


class RedisKeyHandler(type):

    def __new__(cls, name, bases, attrs):

        allowed_commands = []
        for base in bases:
            if not hasattr(base, 'allowed_commands'):
                continue
            allowed_commands.extend(base.allowed_commands)

        for command in allowed_commands:
            if command in attrs:
                continue
            attrs[command] = wrapped_redisext_method(command)
            if not attrs.get('KEY'):
                attrs[command] = classmethod(attrs[command])

        if attrs.get('KEY'):
            key = attrs['KEY']

            def wrapped_method(func):
                @wraps(func)
                def wrapper(cls, *args, **kwargs):
                    return func(cls, key, *args, **kwargs)
                return classmethod(wrapper)
            for attrname, attrvalue in attrs.items():
                if attrname not in allowed_commands:
                    continue
                attrs[attrname] = wrapped_method(attrvalue)
            if 'delete_key' not in attrs:
                attrs['delete_key'] = wrapped_redisext_method('delete')
                attrs['delete_key'] = wrapped_method(attrs['delete_key'])
        else:
            if 'delete_key' not in attrs:
                attrs['delete_key'] = wrapped_redisext_method('delete')
        return super(RedisKeyHandler, cls).__new__(cls, name, bases, attrs)
