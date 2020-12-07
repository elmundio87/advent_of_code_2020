#!/usr/bin/env python3

inputFile = "input.txt"

with open(inputFile, 'r') as stream:
    lines = stream.read().splitlines()\

lines.append("")


bagList = {}

for line in lines:
  bagName = line.split(" bags contain ")[0]
  subBags = {}
  if line:
    for subBag in line.split(" bags contain ")[1].split(","):
      subBagAmount = subBag.strip(" ").strip(".").split(" ")[0]
      subBagName = ' '.join(subBag.strip(" ").strip(".").split(" ")[1:-1])
      subBags[subBagName] = subBagAmount
    bagList[bagName] = subBags

topLevelResults = []
totalResults = []
nextNextLevelResults = []

topLevelResults = list(filter(lambda a: bagList[a].get('shiny gold'), bagList.keys()))
totalResults += topLevelResults
nextLevelResults = topLevelResults
stop = False
while stop == False:
  totalLen = len(totalResults)
  for bagName in nextLevelResults:
    nextNextLevelResults += list(filter(lambda a: bagList[a].get(bagName), bagList.keys()))
    totalResults += nextNextLevelResults
  totalResults = list(set(totalResults))
  if totalLen == len(totalResults):
    stop = True
  nextLevelResults = nextNextLevelResults

print(len(list(set(totalResults))))
