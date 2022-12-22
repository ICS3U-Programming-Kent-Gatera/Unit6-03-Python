#!/usr/bin/env python3

# Created by : Kent G
# Date: Dec. 21, 2022
# This program prints the lowest value of ten randomly
# generated numbers.

import random
import constants


def lowestRandNum(list_of_num):
    # Defining the least number just outside of the range of random numbers.
    lowest_num = 101
    # Iterating over every element in the list to find out which is lesser.
    for num in list_of_num:
        if num < lowest_num:
            lowest_num = num
    return lowest_num


def main():
    # Defining variables.
    rand_num_list = []
    # Getting random numbers to fill up the random number array/list.
    for i in range(0, constants.MAX_ARRAY_SIZE):
        random_num = random.randint(constants.MIN_NUM, constants.MAX_NUM)
        rand_num_list.append(random_num)
    final_num = lowestRandNum(rand_num_list)
    print(f"{rand_num_list}\n")
    # Displaying the smallest random number.
    print(f"The smallest number in the list is {final_num}")


if __name__ == "__main__":
    main()
