#!/usr/bin/env python3

def parseInstruction(line):
  return line.split(" ")

def swapInstruction(line):
  instruction = parseInstruction(line)
  if instruction[0] == "jmp":
    return "{0} {1}".format("nop",instruction[1])
  if instruction[0] == "nop":
    return "{0} {1}".format("jmp",instruction[1])
  return line


def runProgram(lines):
  index = 0
  instructionTracker = []
  acc = 0
  loop = False
  while index not in instructionTracker:
    if(index >= len(lines)):
      return acc,loop
    instruction = parseInstruction(lines[index])
    instructionTracker.append(index)
    if(instruction[0] == "nop"):
      index += 1

    if(instruction[0] == "acc"):
      acc += int(instruction[1])
      index += 1

    if(instruction[0] == "jmp"):
      index += int(instruction[1])



  if(index < len(lines)):
    # print("WARNING: Program executed early due to infinite loop")
    # print("Index",index)
    # print("Instruction", instruction)
    # print("Index stack", instructionTracker)
    loop=True
  return acc,loop

print("Part 1")
with open("input.txt", 'r') as stream:
    lines = stream.read().splitlines()

print(runProgram(lines))

print("Part 2")
for x in range(0, len(lines)):
  lines_temp = lines[:]
  lines_temp[x] = swapInstruction(lines_temp[x])
  result = runProgram(lines_temp)
  if(not result[1]):
    print(result)

