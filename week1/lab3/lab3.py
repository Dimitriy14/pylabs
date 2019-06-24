#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import seed
from random import randint
from time import time


def randomizer(seedkey):
    seed(seedkey)

    return [randint(0, 99) for i in range(50)]


def validateRange(min_num, max_num):
    if max_num <= min_num:
        raise ValueError


def getIndexesOfElementsInRange(min_num, max_num, randomized_list = randomizer(int(time()))):
    validateRange(min_num, max_num)

    new_list = []

    for i, val in enumerate(randomized_list):
        if min_num <= val <= max_num:
            print("list[" + str(i) + "] => " + str(val))
            new_list.append(i)

    return new_list


def main():
    try:
        min_num = int(input("Enter minimum number: "))
        max_num = int(input("Enter maximum number: "))

        print("Result list: ", getIndexesOfElementsInRange(min_num, max_num))
    except ValueError:
        print("Incorrect input or range is invalid, try again.")
        exit(2)
    except Exception as e:
        print("Unexpected exception: ", e)
        exit(127)


if __name__ == "__main__":
    main()
