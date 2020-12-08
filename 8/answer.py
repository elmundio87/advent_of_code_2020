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


def runProgram(lines, debug):
  pc = 0
  instructionTracker = []
  acc = 0
  loop = False
  while pc not in instructionTracker:
    if(pc >= len(lines)):
      return acc,loop
    instruction = parseInstruction(lines[pc])
    instructionTracker.append(pc)
    if(instruction[0] == "nop"):
      pc += 1

    if(instruction[0] == "acc"):
      acc += int(instruction[1])
      pc += 1

    if(instruction[0] == "jmp"):
      pc += int(instruction[1])

    if debug :
      print(instruction, acc)

  if(pc < len(lines)):
    if(debug):
      print("WARNING: Program executed early due to infinite loop")
      print("Program Counter",pc)
      print("Current Instruction", instruction)
      print("Instruction Stack", instructionTracker)
    loop=True
  return acc,loop

print("Part 1")
with open("input.txt", 'r') as stream:
    lines = stream.read().splitlines()

print(runProgram(lines, True))

print("Part 2")
for x in range(0, len(lines)):
  lines_temp = lines[:]
  lines_temp[x] = swapInstruction(lines_temp[x])
  result = runProgram(lines_temp, False)
  if(not result[1]):
    print(result)

