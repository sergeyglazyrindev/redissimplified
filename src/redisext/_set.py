from ._metaclass import RedisKeyHandler


class Set(object, metaclass=RedisKeyHandler):

    allowed_commands = ('sadd', 'scard', 'sismember', 'smembers', 'spop', 'srandmember', 'srem')


class SortedSet(object, metaclass=RedisKeyHandler):

    allowed_commands = ('zadd', 'zcard', 'zcount', 'zincrby', 'zrem', 'zrangebyscore', 'zremrangebyscore',
                        'zrevrangebyscore', 'zscore')
