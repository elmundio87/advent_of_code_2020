#!/usr/bin/env python3

inputFile = "input.txt"

with open(inputFile, 'r') as stream:
    lines = stream.read().splitlines()\


lines = list(map(lambda a: int(a), lines))

def isSum(num, numList):
  for x in range(0,len(numList)):
    for y in range(0,len(numList)):
      if x != y and numList[x] + numList[y] == num:
        return True
  return False

def findSumSet(num, numList):
  for x in range(0,len(numList)):
      for y in range(0,len(numList)):
        if y > x:
          if sum(numList[x:y]) == num:
            sumList = sorted(numList[x:y])
            return sum([sumList[0],sumList[-1]])


print("Part 1")

index = 25
for num in lines[25:]:
  if (not isSum(num, lines[index-25:index])):
    partTwoInput = num
  index += 1

print(partTwoInput)

print("Part 2")

print(findSumSet(partTwoInput, lines))