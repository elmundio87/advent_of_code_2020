#!/usr/bin/env python3

from math import prod

inputFile = "input.txt"

with open(inputFile, 'r') as stream:
    lines = stream.read().splitlines()

def turn(angle, change):
  angle += change

  if angle < 0:
    angle = 360 + angle

  if angle >= 360:
    angle = angle - 360

  return angle

angle = 90

angles = {
  0 : "N",
  90: "E",
  180: "S",
  270: "W"
}

coords = {
  "y": 0,
  "x": 0,
}

def getAngleFromDirection(direction):
  for key in angles:
    if angles[key] == direction:
        return key

def updateWaypoint(direction, speed):
  global waypoint
  if direction == "N":
    waypoint["y"] += speed
  if direction == "S":
    waypoint["y"] -= speed
  if direction == "E":
    waypoint["x"] += speed
  if direction == "W":
    waypoint["x"] -= speed


def forward(angle, speed):
  global coords
  if angle == 0:
    coords["y"] += speed
  if angle == 180:
    coords["y"] -= speed
  if angle == 90:
    coords["x"] += speed
  if angle == 270:
    coords["x"] -= speed

def forwardToWaypoint(speed):
  global coords
  coords["x"] += waypoint["x"] * speed
  coords["y"] += waypoint["y"] * speed

def turnWaypoint(angle):

  x = waypoint["x"]
  y = waypoint["y"]

  if angle < 0:
    angle += 360
  if angle == 90:
    waypoint["x"] = y
    waypoint["y"] = -x
  if angle == 180:
    waypoint["x"] = -x
    waypoint["y"] = -y
  if angle == 270:
    waypoint["x"] = -y
    waypoint["y"] = x


for line in lines:
  order = line[0:1]
  if order in ("N","S","E","W"):
    speed = int(line[1:])
    forward(getAngleFromDirection(order), speed)
  if order in ("L","R","F"):
    if order == "F":
      speed = int(line[1:])
      forward(angle, speed)
    if order == "L":
      angle = turn(angle, int(line[1:]) * -1)
    if order == "R":
      angle = turn(angle, int(line[1:]))

print("Part 1")
print(abs(coords["x"]) + abs(coords["y"]))

waypoint = {
  "y": 1,
  "x": 10,
}

coords = {
  "y": 0,
  "x": 0,
}

for line in lines:
  order = line[0:1]
  if order in ("N","S","E","W"):
    speed = int(line[1:])
    updateWaypoint(order, speed)
  if order in ("L","R","F"):
    if order == "F":
      speed = int(line[1:])
      forwardToWaypoint(speed)
    if order == "L":
      turnWaypoint(int(line[1:]) * -1)
    if order == "R":
      turnWaypoint(int(line[1:]))


print("Part 2")
print(coords)
print(abs(coords["x"]) + abs(coords["y"]))