#!/usr/bin/env python3

inputFile = "input.txt"

with open(inputFile, 'r') as stream:
    lines = stream.read().splitlines()\

lines.append("")

def generateBagList(lines):
  bagList = {}
  for line in lines:
    bagName = line.split(" bags contain ")[0]
    subBags = {}
    if line:
      for subBag in line.split(" bags contain ")[1].split(","):
        subBagAmount = subBag.strip(" ").strip(".").split(" ")[0]
        subBagName = ' '.join(subBag.strip(" ").strip(".").split(" ")[1:-1])
        if subBagAmount != "no":
          subBags[subBagName] = int(subBagAmount)
      if bagName != "other":
        bagList[bagName] = subBags
  return bagList

bagList = generateBagList(lines)
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

print("Part 1")
print(len(list(set(totalResults))))

# Part 2

def get_children(bag):
  child_map = {}
  for sub_bag in bagList[bag]:
    child_map[sub_bag] = get_children(sub_bag)
  if child_map:
    return child_map
  else:
    return

def lookUpNumberOfBags(bag,subBag):
  return bagList[bag][subBag]

def addUpBags(bagTree, parentBag, total=0):
  for bag in bagTree:
    total += lookUpNumberOfBags(parentBag,bag)
    if bagTree[bag]:
      total += (lookUpNumberOfBags(parentBag,bag) * addUpBags(bagTree[bag],bag))
  return total

totalBags = addUpBags(get_children('shiny gold'), 'shiny gold')

print("Part 2")
print(totalBags)
