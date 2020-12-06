#!/usr/bin/env python3

inputFile = "input.txt"

with open(inputFile, 'r') as stream:
    lines = stream.read().splitlines()\

lines.append("")

# Part 1

groups = []
group = []
for line in lines:
  if(line):
    group.append(line)
  else:
    groups.append(group)
    group = []

totalQuestions = 0
for group in groups:
  totalQuestions += len(list(set("".join(group))))

print("Part 1")
print(totalQuestions)

# Part 2

allYes = 0

for group in groups:
  joined_group = "".join(group)
  anyYes = list(set(joined_group))
  for answer in anyYes:
    if len(list(filter(lambda a: a == answer, joined_group))) == len(group):
      allYes += 1

print("Part 2")
print(allYes)

