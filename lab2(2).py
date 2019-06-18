from random import seed
from random import randint

# generate first set
seed(1)
first_set = {randint(0, 10) for i in range(10)}

# generate second set
seed(7)
second_set = {randint(0, 10) for j in range(10)}

print("First set: ", first_set)
print("Second set: ", second_set)

print("Amount of similar number", len(first_set.intersection(second_set)))