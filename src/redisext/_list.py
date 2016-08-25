from ._metaclass import RedisKeyHandler
from future.utils import with_metaclass


class List(with_metaclass(RedisKeyHandler, object)):

    allowed_commands = ('llen', 'lpush', 'lpop')
