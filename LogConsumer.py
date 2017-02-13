import logging

from LogConsumerChild import child


def consume_log():
    logging.error("I ran. here do you know???")
    child()