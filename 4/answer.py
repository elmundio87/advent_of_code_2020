#!/usr/bin/env python3


import re

inputFile = "input.txt"

with open(inputFile, 'r') as stream:
    lines = stream.read().splitlines()

def validateHeight(val):
  if(val[-2:] == "cm"):
    return int(val[0:-2]) in range(150,193+1)
  elif(val[-2:] == "in"):
    return int(val[0:-2]) in range(59,76+1)
  else:
    return False


temp_passport = {}
passports = []
requiredFields = [
  ["byr", lambda a : int(a) in range(1920,2002+1)],
  ["iyr", lambda a : int(a) in range(2010,2020+1)],
  ["eyr", lambda a : int(a) in range(2020,2030+1)],
  ["hgt", lambda a : validateHeight(a)],
  ["hcl", lambda a : re.search("^#[0-9|a-f]{6}$",a) != None],
  ["ecl", lambda a : a in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]],
  ["pid", lambda a : re.search("^[0-9]{9}$",a) != None]
]

for line in lines:
  if line:
    properties = line.split(" ")
    for prop in properties:
      key = prop.split(":")[0]
      value = prop.split(":")[1]
      temp_passport[key] = value
  else:
    passports.append(temp_passport)
    temp_passport = {}

for passport in passports:
  passport['valid'] = True
  for field in requiredFields:
    if not passport.get(field[0]):
      passport['valid'] = False

print("Part 1")
validPassports = list(filter(lambda a : a.get('valid'), passports))
print(len(validPassports))

print("Part 2")

for passport in passports:
  passport['valid'] = True
  for field in requiredFields:
    if not passport.get(field[0]):
      passport['valid'] = False
    else:
      if not field[1](passport[field[0]]):
        passport['valid'] = False

validPassports = list(filter(lambda a : a.get('valid'), passports))
print(len(validPassports))