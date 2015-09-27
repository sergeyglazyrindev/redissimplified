from ._metaclass import RedisKeyHandler


class Hash(object, metaclass=RedisKeyHandler):

    allowed_commands = ('hdel', 'hexists', 'hget', 'hgetall', 'hincrby', 'hincrbyfloat',
                        'hkeys', 'hlen', 'hset', 'hmset', 'hmget', 'hvals', 'hstrlen')
