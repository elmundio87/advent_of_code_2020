#!/usr/bin/env python3

import math

inputFile = "input.txt"

with open(inputFile, 'r') as stream:
    lines = stream.read().splitlines()\

def getSeatId(line):
  rowUpper = 127
  rowLower = 0
  columnUpper = 7
  columnLower = 0

  for instruction in line:
    if instruction == "F" :
      rowUpper = math.floor((rowUpper-rowLower)/2) + rowLower
    elif instruction == "B":
      rowLower = math.ceil((rowUpper-rowLower)/2) + rowLower
    elif instruction == "L":
      columnUpper = math.floor((columnUpper-columnLower)/2) + columnLower
    elif instruction == "R":
      columnLower = math.ceil((columnUpper-columnLower)/2) + columnLower

  return (rowLower * 8) + columnLower

highestSeatId = 0

for line in lines:
  newSeatId = getSeatId(line)
  if newSeatId > highestSeatId:
    highestSeatId = newSeatId


print("Part 1")
print(highestSeatId)

print("Part 2")

seatIds = sorted(list(map(lambda a: getSeatId(a), lines)))
for seatIndex in range(1, len(seatIds)):
  if seatIds[seatIndex]-1 != seatIds[seatIndex-1]:
    print(seatIds[seatIndex]-1)
