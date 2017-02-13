import logging
from LogConsumer import consume_log

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
# file log handler
fh =logging.FileHandler('example.log',)
#console log handler
# ch =logging.StreamHandler()
# levels for loggers
fh.setLevel(logging.DEBUG)
# ch.setLevel(logging.INFO)
#formatter
formatter = logging.Formatter('%(levelname)-8s %(asctime)-25s %(filename)-20s %(funcName)-12s %(message)-40s %(process)d')
#set formatters for loggers
fh.setFormatter(formatter)
# ch.setFormatter(formatter)

#add handlers
logger.addHandler(fh)
# TODO make this as a utility one place for log.
# TODO single file for logging
# TODO make this configurable
def main():
    logger.critical('This is a critical message.')
    logger.error('This is an error message')
    logger.warning('This is a warning message.')
    logger.info('This is an informative message.')
    logger.debug('This is a low-level debug message')
    consume_log()

if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser(description='Log Utility')
    # get optional(optional param) log level default-WARNING
    parser.add_argument('-ll', '--loglevel',
                        type=str,
                        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
                        help='Set the logging level')
    args = parser.parse_args()
    # logging.basicConfig(level=args.loglevel)
    main()