import logging as log
from os import mkdir

from src.api.prj1.parse_input import parse_input

def main():
    with open('data_1.txt', 'r') as f:
        l = [[int(num) for num in line.split(' ')] for line in f]
        parse_input(l)

def prepare():
    # create logs directory if does not exist already
    try:
        mkdir('logs')
    except:
        pass

    # create or clear the file
    with open('logs/runtime.log', 'w'):
        pass

    # setup the config of the logger
    log.basicConfig(
        filename='logs/runtime.log',
        encoding='utf-8',
        format='%(levelname)s | %(asctime)s | %(filename)s:%(lineno)s | %(funcName)s() | %(message)s',
        datefmt='%Y/%m/%d | %H:%M:%S',
        level='INFO')
    log.info("Logger setup finished")

if __name__ == "__main__":
    prepare()
    main()
