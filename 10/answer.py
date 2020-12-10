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


def addToChain(chain,index=0):
  currentLink = chain[index]
  for nextLinkIndex in range(index, len(chain)):
    if index == len(chain)-1:
      global total
      total += 1
      return

    if chain[nextLinkIndex] - currentLink in range(1,4):
      addToChain(chain, nextLinkIndex)

  if index == 0:
    return total
  else:
    return

total = 0
chainTree = addToChain(chain)
print(chainTree)