#Write a program that generates 100 random 
# integers that are either 0 or 1. Then find the
#longest run of zeros, the largest number 
# of zeros in a row. For instance, the longest run of
#zeros in [1,0,1,1,0,0,0,0,1,0,0] is 4.

import random

random_list = [random.randint(0, 1) for _ in range(100)]
print(random_list)

max_zeros = 0
current_zeros = 0

for num in random_list:
    if num == 0:
        current_zeros += 1
        max_zeros = max(max_zeros, current_zeros)
    else:
        current_zeros = 0

print("Longest run of zeros:", max_zeros)

        
