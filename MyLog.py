import logging
logger = logging.getLogger()

def main():
    logger.critical('This is a critical message.')
    logger.error('This is an error message.')
    logger.warning('This is a warning message.')
    logger.info('This is an informative message.')
    logger.debug('This is a low-level debug message.')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()