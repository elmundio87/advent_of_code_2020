#!/usr/bin/env python3

inputFile = "input.txt"

with open(inputFile, 'r') as stream:
    lines = stream.read().splitlines()

grid = []
for line in lines:
  gridLine = list(line)
  grid.append(gridLine)

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

print(occupiedSeats)

