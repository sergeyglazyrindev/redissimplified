import mock
from unittest import TestCase

from src.redisext import (
    ConnectionHandler,
    List,
)


class TestConnectionHandler(ConnectionHandler):
    connection = None


class TestList(List, ConnectionHandler):
    KEY = 'testlist'

    @classmethod
    def method(cls, *args):
        cls._method(*args)

    @classmethod
    def _method(cls, *args):
        pass


class TestRedisExt(TestCase):

    def test_metaclass_handler(self):
        with mock.patch.object(TestList, '_method') as _mocked_method,\
                mock.patch('redis.StrictRedis.llen') as _redis_mocked:
            TestList.method('1', '2')
            self.assertEqual(_mocked_method.call_args, mock.call('1', '2'))
            TestList.llen()
            self.assertEqual(_redis_mocked.call_args, mock.call('testlist', ))

    def test_delete_key_method(self):
        with mock.patch('redis.StrictRedis.delete') as _redis_mocked:
            TestList.delete_key()
            self.assertEqual(_redis_mocked.call_args, mock.call('testlist', ))
