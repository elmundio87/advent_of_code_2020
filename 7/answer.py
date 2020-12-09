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
      if subBagAmount != "no":
        subBags[subBagName] = int(subBagAmount)
    if bagName != "other":
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

print("Part 1")
print(len(list(set(totalResults))))

inputFile = "input2.txt"

with open(inputFile, 'r') as stream:
    lines = stream.read().splitlines()\

lines.append("")

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

def addUpBags(bagTree, parentBag):
  for bag in bagTree:
    if bagTree[bag]:
      addUpBags(bagTree[bag],bag)

bagtree = bagList['shiny gold']
totalBags = 0
index = 0
stop = False
# while not stop:

result = get_children('shiny gold')
print(result)
totalBags = 0
addUpBags(result, 'shiny gold')



print("Part 2")
print(totalBags)
