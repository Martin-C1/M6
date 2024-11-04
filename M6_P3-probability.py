#Martin Cahue
# October 31, 2024

import random
heads_probability = 72/100
tails_probability = 28/100
#defines that the heads probability is 72 and tails probability is 28
heads_number = 0
tails_number = 0
#defines the total of heads and tails as 0 before the 1000 coin flips
for i in range(1000):
    if random.random() < heads_probability:
        heads_number += 1
    else:
        tails_number += 1
#flips a coin 1000 times and adds 1 to heads if the random number is less than 72, otherwise it adds 1 to tails
percentage_heads = (heads_number / 1000) * 100
percentage_tails = (tails_number / 1000) * 100
print(f"The coin shows Heads {percentage_heads:.2f}% of the time")
print(f"The coin shows tails {percentage_tails:.2f}% of the time")
#P3- a program that executes a probabilistic event