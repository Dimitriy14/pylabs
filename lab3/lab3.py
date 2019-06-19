from random import seed
from random import randint
from time import time


def randomizer(seedkey):
    seed(seedkey)
    rand_list = [randint(0, 99) for i in range(50)]
    return rand_list


def get_indexes(some_list, min_num=1, max_num=99):
    new_list = []
    for i, val in enumerate(some_list):
        if min_num <= val <= max_num:
            print("list[" + str(i) + "] => " + str(val))
            new_list.append(i)
    return new_list


def main():
    randomized_list = randomizer(int(time()))
    print("Generated list: ", randomized_list)

    try:
        min_num = int(input("Enter minimum number: "))
        max_num = int(input("Enter maximum number: "))
        if max_num <= min_num:
            print("Wrong numspace, try again.")
            exit(1)
        print("Result list: ", get_indexes(randomized_list, min_num, max_num))
    except ValueError:
        print("Incorrect input, try again.")
        exit(2)
    except Exception as e:
        print("Unexpected exception: ", e)
        exit(127)


if __name__ == "__main__":
    main()
