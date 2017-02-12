import logging

from LogConsumerChild import child


def consume_log():
    logging.debug("I ran. here do you know???")
    child()