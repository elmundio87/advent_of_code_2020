#!/usr/bin/env python3

inputFile = "input.txt"

with open(inputFile, 'r') as stream:
    lines = stream.read().splitlines()

def setUpGrid(lines):
  grid = []
  for line in lines:
    gridLine = list(line)
    grid.append(gridLine)
  return grid

def flatten(l1):
  flat=[]
  for i in l1:
    for j in i:
      flat.append(j)
  return flat

def countAdjacentSeatsOccupied(y,x,grid):
  count = 0
  for y1 in range(y-1, y+2):
    for x1 in range(x-1, x+2):
      centre = (x1 == x and y1 == y)
      outOfBounds = (y1 < 0 or y1 >= len(grid) or x1 < 0 or x1 >= len(grid[0]))
      if not outOfBounds and not centre:
        if grid[y1][x1] == "#":
          count += 1
  return count

def visibleOccupiedSeatInDirection(y,x,y1,x1,grid):

  if y1 == 0 and x1 == 0:
    return 0

  outOfBounds = False
  while True:
    outOfBounds = (y+y1 < 0 or y+y1 >= len(grid) or x+x1 < 0 or x+x1 >= len(grid[0]))
    if outOfBounds:
      return 0
    else:
      y += y1
      x += x1
    if grid[y][x] == "L":
      return 0
    if grid[y][x] == "#":
      return 1

  return 0

grid = setUpGrid(lines)

count = 0
nextGrid = []
nextGrid = [x[:] for x in grid]

while flatten(grid) != flatten(nextGrid) or count == 0:
  grid = [x[:] for x in nextGrid]
  for y in range(0,len(grid)):
    for x in range(0,len(grid[0])):
      if grid[y][x] == "L":
        if countAdjacentSeatsOccupied(y,x,grid) == 0:
          nextGrid[y][x] = "#"
      if grid[y][x] == "#":
        if countAdjacentSeatsOccupied(y,x,grid) >= 4:
          nextGrid[y][x] = "L"
  count += 1

occupiedSeats = 0

for y in range(0,len(grid)):
  for x in range(0,len(grid[0])):
     if grid[y][x] == "#":
       occupiedSeats += 1

print("Part 1")
print(occupiedSeats)

grid = setUpGrid(lines)

count = 0
nextGrid = []
nextGrid = [x[:] for x in grid]

while flatten(grid) != flatten(nextGrid) or count == 0:
  grid = [x[:] for x in nextGrid]
  for y in range(0,len(grid)):
    for x in range(0,len(grid[0])):
      visibleSeats = 0
      if grid[y][x] == "L":
        for y1 in range(-1, 2):
          for x1 in range(-1, 2):
            visibleSeats += visibleOccupiedSeatInDirection(y,x,y1,x1, grid)
        if visibleSeats == 0:
          nextGrid[y][x] = "#"
      if grid[y][x] == "#":
        for y1 in range(-1, 2):
          for x1 in range(-1, 2):
            visibleSeats += visibleOccupiedSeatInDirection(y,x,y1,x1, grid)
        if visibleSeats >= 5:
          nextGrid[y][x] = "L"
  count += 1

occupiedSeats = 0

for y in range(0,len(grid)):
  for x in range(0,len(grid[0])):
     if grid[y][x] == "#":
       occupiedSeats += 1
print("Part 2")
print(occupiedSeats)