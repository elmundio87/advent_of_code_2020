#!/usr/bin/env python3
inputFile = "input.txt"

with open(inputFile, 'r') as stream:
    lines = stream.read().splitlines()

def revealMap(n):
  return n*100

fullMap = list(map(revealMap,lines))

def countTrees(map, angle):

  treeCount = 0
  currentCoords = [0,0]
  treeMarker = "#"

  while currentCoords[0] < len(fullMap):

    if fullMap[currentCoords[0]][currentCoords[1]] == treeMarker:
      treeCount += 1

    currentCoords[0] += angle[0]
    currentCoords[1] += angle[1]

  return treeCount

# Part 1

print("Part 1:")
print(countTrees(fullMap, [1,3]))

# Part 2

print("Part 2")
print(countTrees(fullMap,[1,1])*countTrees(fullMap,[1,3])*countTrees(fullMap,[1,5])*countTrees(fullMap,[1,7])*countTrees(fullMap,[2,1]))
