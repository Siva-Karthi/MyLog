import logging
logger = logging.getLogger()

def main():
    logger.critical('This is a critical message.')
    logger.error('This is an error message.')
    logger.warning('This is a warning message.')
    logger.info('This is an informative message.')
    logger.debug('This is a low-level debug message.')


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser(description='Log Utility')
    # get optional(NOT REQUIRED) log level default-WARNING
    parser.add_argument('-ll', '--loglevel',
                        type=str,
                        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
                        help='Set the logging level')
    args = parser.parse_args()
    logging.basicConfig(level=args.loglevel)
    main()