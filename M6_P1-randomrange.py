#Martin Cahue
#October 31, 2024

import random
rand_nums = []
#creates a list called rand_nums where the 10 random integers are stored
for i in range(10):
    random_number = random.randrange(25, 36)
#generates 10 random numbers from 25 to 35 and saves it as random_number
    rand_nums.append(random_number)
#numbers in random_number are added to the list "rand_nums"
    print(random_number)
#P1- a program that prints 10 random integers between 25 and 35