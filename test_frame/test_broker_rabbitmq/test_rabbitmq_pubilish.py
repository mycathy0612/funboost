import random
import time

from test_frame.test_broker_rabbitmq.test_rabbitmq_consume import test_fun
from funboost import PriorityConsumingControlConfig

test_fun.clear()
for i in range(10):
    test_fun.push(i)
time.sleep(10000)
