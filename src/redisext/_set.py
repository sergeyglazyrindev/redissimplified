from ._metaclass import RedisKeyHandler
from future.utils import with_metaclass


class Set(with_metaclass(RedisKeyHandler, object)):

    allowed_commands = ('sadd', 'scard', 'sismember', 'smembers', 'spop', 'srandmember', 'srem')


class SortedSet(with_metaclass(RedisKeyHandler, object)):

    allowed_commands = ('zadd', 'zcard', 'zcount', 'zincrby', 'zrem', 'zrangebyscore', 'zremrangebyscore',
                        'zrevrangebyscore', 'zscore')
