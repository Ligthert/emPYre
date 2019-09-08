#!/usr/bin/env python3

import noise
import random

map_width = 150
map_height = 50

def printMap(map):
  row_nr = 0
  for row in map:
    print(str(row_nr)+":"+str(row))
    row_nr = row_nr+1

def printWorld(map):
  for row in map:
    for cell in row:
      if cell>0:
        print('\x1b[1;37;42m' + ' ' + '\x1b[0m', end='')
      else:
        print('\x1b[1;37;44m' + ' ' + '\x1b[0m', end='')
    print("")

def countLand(map):
  land = 0
  cells = 0
  for row in map:
    for cell in row:
      if cell>0:
        land=land+1
      cells=cells+1
  print("Total Land: "+str(land)+" out of "+str(cells)+" cells. Percentage of land is "+str(land/(cells/100)))

#def printXbar(150):

# Find coastal positions
def findCoast(map):

  # Generate an empty map to put a map of the coast in there
  map_coast = [[0 for x in range(map_width)] for y in range(map_height)]

  # Starting positions!
  y = 0
  x = 0

  while y < map_height:
    x = 0
    while x < map_width:
      water = 0
      if x !=0 and x!=(map_width-1) and y!=0 and y!=(map_height-1) and map[y][x]>0:
        if isWater(map,x-1,y-1):
          water += 1
        if isWater(map,x,y-1):
          water += 1
        if isWater(map,x+1,y-1):
          water += 1
        if isWater(map,x+1,y):
          water += 1
        if isWater(map,x+1,y+1):
          water += 1
        if isWater(map,x,y+1):
          water += 1
        if isWater(map,x-1,y+1):
          water += 1
        if isWater(map,x-1,y):
          water += 1
      if water >= 1:
        map_coast[y][x] = 1
      x+=1
    y+=1
  return map_coast

def isWater(map,x,y):
  if map[y][x] < 0:
    return True
  else:
    return False

scale = 32
octaves = 50
persistence = 0.5
lacunarity = 1.25 + random.random()
base=random.randint(1,250)

map = [[0 for x in range(map_width)] for y in range(map_height)]

for x in range(map_width):
  for y in range(map_height):
    map[y][x]=noise.pnoise2( x/scale, y/(scale/3), octaves=octaves, persistence=persistence, lacunarity=lacunarity, repeatx=map_width, repeaty=map_height, base=base ) * 128

#printMap(map)
printWorld(map)
countLand(map)
print("---")
map_coast = findCoast(map)
printWorld(map_coast)

# TODO:
# - countLand(map) returns a list of coordinates
# - findCoast(map) returns a list of coordinates
# - generateCities(map,map_coast,percentage_on_cost) returns map of cities
