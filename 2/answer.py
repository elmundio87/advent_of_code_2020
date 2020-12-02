#!/usr/bin/env python3

inputFile = "input.txt"

with open(inputFile, 'r') as stream:
    lines = stream.read().splitlines()

part1_count = 0 # Track correct answers to part one
part2_count = 0 # Track correct answers to part two

for line in lines:

  var_range = line.split(" ")[0]
  range_lower = int(var_range.split('-')[0])
  range_upper = int(var_range.split('-')[1])

  letter = line.split(" ")[1][0]

  password = line.split(" ")[2]

  #  Using str.count to work out how many instances of a substring exist in a string
  if(password.count(letter) <= range_upper and password.count(letter) >= range_lower):
    part1_count += 1

  # Use the XOR operator to work out if only one of the conditions is true
  if(bool(password[range_lower-1] == letter) ^ bool(password[range_upper-1] == letter)):
    part2_count += 1

print("Part 1")
print(part1_count)
print ("Part 2")
print(part2_count)