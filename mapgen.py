#!/usr/bin/env python3

WATER=50
SMOOTH=50

MAX_WIDTH = 20
MAX_HEIGHT = 10
MAP_SIZE = MAX_WIDTH * MAX_HEIGHT
NUM_CITY = ((100 * (MAX_WIDTH + MAX_HEIGHT)) / 228)

INFINITY = 10000000

# There are 3 maps.  'map' describes the world as it actually exists; it tells whether each map cell is land, water or a city; it tells whether or not a square is on the board.
# 'user_map' describes the user's view of the world.  'comp_map' describes the computer's view of the world.

class bcolors:
  HEADER = '\033[95m'
  BLUE = '\033[94m'
  GREEN = '\033[92m'
  YELLOW = '\033[93m'
  RED = '\033[91m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'
  ENDC = '\033[0m'

def print_land():
  return bcolors.GREEN+"+"+bcolors.ENDC

def print_water():
  return bcolors.BLUE+"."+bcolors.ENDC

def print_city(side):
  if side=="player":
    return bcolors.BOLD+"O"+bcolors.ENDC
  elif side=="enemy":
    return bcolors.RED+"*"+bcolors.ENDC
  elif side=="neutral":
    return "*"

if __name__=="__main__":
  for y in range(0,MAX_HEIGHT):
    row = ""
    for x in range(0,MAX_WIDTH):
      row = row+print_land()
    print(row)

# print(print_land()+print_land()+print_water()+print_land()+print_city("neutral")+print_land())
# print(bcolors.YELLOW+"WARNING: "+bcolors.RED+"You are a cuck!"+bcolors.ENDC+" "+bcolors.UNDERLINE+"(sorta)"+bcolors.ENDC+" "+bcolors.BOLD+"hihi"+bcolors.ENDC+" \x1b[6;30;42m haha!! ")

# Ref: https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-terminal-in-python
#Friendly+Land:
# print('\x1b[1;37;42m' + 'Success!' + '\x1b[0m')
#Vijand+land
# print('\x1b[1;31;42m' + 'a' + '\x1b[0m')

#Friendly+Sea:
# print('\x1b[1;37;44m' + 'Success!' + '\x1b[0m')
#Vijand+Sea:
# print('\x1b[1;31;44m' + 'B' + '\x1b[0m')
