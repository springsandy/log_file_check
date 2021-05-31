import logging
from file import file_r

def main():
    logger = logging.getLogger(__name__)

    formatter = logging.Formatter('%(asctime)s %(levelname)s %(filename)s:%(lineno)s %(message)s')

    streamHandler = logging.StreamHandler()
    fileHandler = logging.FileHandler('./a.log')

    streamHandler.setFormatter(formatter)
    fileHandler.setFormatter(formatter)

    logger.addHandler(streamHandler)
    logger.addHandler(fileHandler)

    logger.setLevel(level=logging.DEBUG)
    logger.debug('my DEBUG log')
    logger.info('my INFO log')
    logger.warning('my WARNING log')
    logger.error('my ERROR log')
    logger.critical('my CRITICAL log')

main()
file_r()