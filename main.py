import logging
import os
from choice import choice

def main():
    logger = logging.getLogger(__name__)

    formatter = logging.Formatter('%(asctime)s, %(levelname)s, %(filename)s, %(lineno)s, %(message)s')

    if os.path.isfile('./a.log'):
        os.remove('./a.log')
    fileHandler = logging.FileHandler('./a.log')

    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)

    logger.setLevel(level=logging.DEBUG)
    logger.debug('my DEBUG log')
    logger.info('my INFO log')
    logger.warning('my WARNING log')
    logger.error('my ERROR log')
    logger.critical('my CRITICAL log')

main()
choice()