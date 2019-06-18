#!/usr/bin/env python                                       
# -*- coding: utf-8 -*-                                     

from random import seed
from random import randint
from time import time


def randomizer(seedkey):
    seed(seedkey)
    rand_list = [randint(0, 99) for i in range(50)]

    return rand_list


def main():
    randomized_list = randomizer(seedkey=int(time()))
    print("Generated list: ", randomized_list)

    new_list = []

    try:
        min_num = int(input("Enter minimum number: "))
        max_num = int(input("Enter maximum number: "))
        if max_num <= min_num:
            print("Wrong numspace, try again.")
            exit(1)
        for i, val in enumerate(randomized_list):
            if min_num <= val <= max_num:
                print("list[" + str(i) + "] => " + str(val))
                new_list.append(i)
        print("Result list: ", new_list)
    except ValueError:
        print("Incorrect input, try again.")
        exit(2)
    except Exception as e:
        print("Unexpected exception: ", e)
        exit(127)


if __name__ == "__main__":
    main()
