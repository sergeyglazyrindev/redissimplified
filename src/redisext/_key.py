from ._metaclass import RedisKeyHandler


class Key(object, metaclass=RedisKeyHandler):

    allowed_commands = ('exists', 'expire', 'expireat', 'pexpire', 'ttl', 'pttl')

    def delete(cls, key):
        return cls._redis().delete(key)
