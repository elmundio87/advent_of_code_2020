#!/usr/bin/env python3

from math import prod

inputFile = "input.txt"

with open(inputFile, 'r') as stream:
    lines = stream.read().splitlines()
    lines_int = [int(i) for i in lines]

# Recursively run through a list of ints and find the product
# lines[int]: A list of values to recurse through
# find_sum: An int value to try and add up to while recursing
# starting_depth: The number of values to find the product of.
#
# eg. To find the product of 3 numbers that add to 2020 in a list;
#
#  product_recurse(lines_int, 2020, 3)
#
#
def product_recurse(lines, find_sum, starting_depth, current_depth=None, values=None):
    if(values == None):
      starting_depth = starting_depth - 1
      values = [0] * (starting_depth + 1)

    if(current_depth == None):
      current_depth = starting_depth

    for x in lines:
      values[starting_depth - current_depth] = x
      if(current_depth > 0):
        product_recurse(lines, find_sum, starting_depth, current_depth-1, values)
      else:
        if(sum(values) == find_sum):
          print(values, ":", prod(values))
          for val in values:
            lines.remove(val)

product_recurse(lines_int, 2020, 2)
product_recurse(lines_int, 2020, 3)


