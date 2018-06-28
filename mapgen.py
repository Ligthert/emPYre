#!/usr/bin/env python3

WATER=50
SMOOTH=50

MAX_WIDTH = 100
MAX_HEIGHT = 60
MAP_SIZE = MAX_WIDTH * MAX_HEIGHT
NUM_CITY = ((100 * (MAP_WIDTH + MAP_HEIGHT)) / 228)

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
#  print(print_land()+print_land()+print_water()+print_land()+print_city("neutral")+print_land())
#  print(bcolors.YELLOW+"WARNING: "+bcolors.RED+"You are a cuck!"+bcolors.ENDC+" "+bcolors.UNDERLINE+"(sorta)"+bcolors.ENDC+" "+bcolors.BOLD+"hihi"+bcolors.ENDC+" \x1b[6;30;42m haha!! ")
