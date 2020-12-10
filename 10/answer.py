#!/usr/bin/env python3

from math import prod

inputFile = "input.txt"

with open(inputFile, 'r') as stream:
    lines = stream.read().splitlines()
    lines_int = [int(i) for i in lines]

chain = sorted(lines_int)
chain.insert(0,0)
chain.append(chain[-1]+3)
diffs = [0] * (3+1)

for index in range(1,len(chain)):
  diffs[chain[index]-chain[index-1]] += 1

print("Part 1")
print(diffs[1]*diffs[3])

print("Part 2")



# Work backwards through the chain, caching
# totals in memory to avoid recalculations
#
# Ref: https://github.com/andrewyazura/aoc-2020/blob/main/day-10/main.py
def findChains(chain, memory):
    total = 0
    lastLink = chain[-1]

    # Fetch value from memory if it exists
    if memory.get(lastLink):
        return memory[lastLink]

    if len(chain) == 1:
        return 1 # Break when there's only 1 element left

    # Check neighbouring links to see if any of them
    # are within a difference of 3
    for i in range(1, 4):
      node = get_item(chain, -i - 1)

      if node is not None and lastLink - node <= 3:
          total += findChains(chain[:-i], memory)

    memory[lastLink] = total
    return total


def get_item(l, index):
  if -len(l) <= index < len(l):
      return l[index]
  return None

memory = {}

print(findChains(chain, memory))
