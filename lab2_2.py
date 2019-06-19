from random import seed
from random import randint
from time import time


def randomizer(seedkey):
    seed(seedkey)
    rand_set = {randint(0, 99) for i in range(50)}

    return rand_set


def main():
    first_set = randomizer(int(time()))
    print("First set: ", first_set)

    second_set = randomizer(int(time())+1)
    print("Second set: ", second_set)

    print("Amount of similar number", len(first_set.intersection(second_set)))


if __name__ == "__main__":
    main()

