from ._metaclass import RedisKeyHandler


class List(object, metaclass=RedisKeyHandler):

    allowed_commands = ('llen', 'lpush', 'lpop')
