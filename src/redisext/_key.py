from ._metaclass import RedisKeyHandler
from future.utils import with_metaclass


class Key(with_metaclass(RedisKeyHandler, object)):

    allowed_commands = ('exists', 'expire', 'expireat', 'pexpire', 'get',
                        'ttl', 'pttl', 'setnx', 'incr', 'incrby', 'decr', 'decrby')

    @classmethod
    def delete(cls, key):
        return cls._redis().delete(key)
