import redis


class ConnectionHandler(object):

    connection = {
        'host': 'localhost',
        'port': 6379,
        'db': 0
    }

    @classmethod
    def _redis(cls):
        return redis.Redis(
            **cls.connection
        )
