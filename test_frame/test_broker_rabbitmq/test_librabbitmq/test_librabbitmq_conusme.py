import requests
from amqp import Message, Connection, ConnectionError, ChannelError
import nb_log
TEST_QUEUE = 'pyrabbit.testq'

connection = Connection(host='192.168.60.106:5672', userid='guest',
                             password='guest', virtual_host='/')
channel = connection.channel()
channel.queue_delete(TEST_QUEUE)

channel.exchange_declare(TEST_QUEUE, 'direct')
x = channel.queue_declare(TEST_QUEUE)
channel.queue_bind(TEST_QUEUE, TEST_QUEUE, TEST_QUEUE)