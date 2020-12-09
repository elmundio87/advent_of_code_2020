#!/usr/bin/env python3

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

# Fetch number of a specific bags that a parent bag can contain
def lookUpNumberOfBags(bag,subBag):
  return bagList[bag][subBag]

# Recursive function to generate a bag dependency tree
def get_children(bag):
  child_map = {}
  for sub_bag in bagList[bag]:
    child_map[sub_bag] = get_children(sub_bag)
  if child_map:
    return child_map
  else:
    return

# Recursive function that adds up the total number of bags within a bag dependency tree
def addUpBags(bagTree, parentBag, total=0):
  for bag in bagTree:
    total += lookUpNumberOfBags(parentBag,bag)
    if bagTree[bag]:
      total += (lookUpNumberOfBags(parentBag,bag) * addUpBags(bagTree[bag],bag))
  return total

# Recursive function that determines if a bag is a direct or transitive dependency on a parent bag
def bagTreeContainsBag(bagTree, bag, searchTerm, returnVal=False):
  if(bagTree):
    for bag in bagTree:
      if bag == searchTerm or bagTreeContainsBag(bagTree[bag], bag, searchTerm):
        returnVal = True
  return returnVal

inputFile = "input.txt"

with open(inputFile, 'r') as stream:
    lines = stream.read().splitlines()\

bagList = generateBagList(lines)

# Part 1

totalResults = 0
for bag in bagList:
  bagTree = get_children(bag)
  if(bagTreeContainsBag(bagTree, bag, 'shiny gold')):
    totalResults += 1

print("Part 1")
print(totalResults)

# Part 2

totalBags = addUpBags(get_children('shiny gold'), 'shiny gold')

print("Part 2")
print(totalBags)
