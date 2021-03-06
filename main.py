import logging as log
import sys
from os import mkdir

import src.exercises.project1 as prj1
import src.exercises.project2 as prj2
import src.exercises.project3 as prj3
import src.exercises.project4 as prj4
import src.exercises.project6 as prj6


def main():
    args = sys.argv[1:]
    prepare(args[0] if len(args) > 0 else "info")

    # prj1.task1()
    # prj1.task2()
    # prj1.task3()

    # prj2.task1()
    # prj2.task2()
    # prj2.task3()
    # prj2.task4()
    # prj2.task5()
    # prj2.task6()

    # prj3.task1_2()
    # prj3.task3()
    # prj3.task4()
    # prj3.task5()

    # prj4.prj_4()

    prj6.example01a()
    # prj6.example01b()
    # prj6.example02inputdata()
    # prj6.example02random2Dgraph()


def prepare(loglevel):
    # create logs directory if does not exist already
    try:
        mkdir("logs")
    except FileExistsError:
        pass

    # create or clear the file
    with open("logs/runtime.log", "w"):
        pass

    # setup the config of the logger
    log.basicConfig(
        filename="logs/runtime.log",
        encoding="utf-8",
        format="%(levelname)s | %(asctime)s | %(filename)s:%(lineno)s | %(funcName)s() | %(message)s",
        datefmt="%Y/%m/%d | %H:%M:%S",
        level=loglevel.upper(),
    )
    log.info("Logger setup finished")


if __name__ == "__main__":
    main()
