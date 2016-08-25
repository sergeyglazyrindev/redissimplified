from ._metaclass import RedisKeyHandler
from future.utils import with_metaclass


class Hash(with_metaclass(RedisKeyHandler, object)):

    allowed_commands = ('hdel', 'hexists', 'hget', 'hgetall', 'hincrby', 'hincrbyfloat',
                        'hkeys', 'hlen', 'hset', 'hmset', 'hmget', 'hvals', 'hstrlen')
