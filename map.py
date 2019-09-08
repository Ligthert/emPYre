import noise
import random
from collections import defaultdict

class Map():

  def __init__( self, width=150, height=50, sealevel=0 ):

    # Dealing with basic params
    self.width = width
    self.height = height
    self.sealevel = sealevel

    # The master map we are going to need
    self.map = defaultdict(dict)
    self.coast = []

    # All the required stuff to determine cities
    self.cities = []
    self.num_cities = 100
    self.coast_percentage = 25


  def generateMap(self):
    # Some precedural stuff that is kinda required
    scale = 32
    octaves = 50
    persistence = 0.5
    lacunarity = 1.25 + random.random()
    base=random.randint(1,250)

    # Fill in the blanks with random stuff
    for y in range(1,self.height+1):
      for x in range(1,self.width+1):
        area = noise.pnoise2( x/scale, y/(scale/3), octaves=octaves, persistence=persistence, lacunarity=lacunarity, repeatx=self.width, repeaty=self.height, base=base ) * 128
        if area > self.sealevel:
          self.map[x][y] = "l"
        else:
          self.map[x][y] = "w"


  # Find coastal positions
  def findCoast(self):
    # Should replace with a range()-loop
    y = 1

    while y <= self.height:
      x = 1
      while x <= self.width:
        water = 0
        if x !=1 and x!=self.width and y!=1 and y!=self.height and self.map[x][y]=="l":
          if self.map[x-1][y-1]=="w":
            water += 1
          if self.map[x][y-1]=="w":
            water += 1
          if self.map[x+1][y-1]=="w":
            water += 1
          if self.map[x+1][y]=="w":
            water += 1
          if self.map[x+1][y+1]=="w":
            water += 1
          if self.map[x][y+1]=="w":
            water += 1
          if self.map[x-1][y+1]=="w":
            water += 1
          if self.map[x-1][y]=="w":
            water += 1
        if water >= 1:
          coords = {}
          coords['x'] = x
          coords['y'] = y
          self.coast.append(coords)
        x+=1
      y+=1


  def generateCities(self):
    for round in range(0,self.num_cities):
      if random.randint(1,100) < self.coast_percentage:
        self.cities.append(random.choice(self.coast))
      else:
        found = 0
        while found == 0:
          randX = random.randint(1,self.width)
          randY = random.randint(1,self.height)
          #print("Round "+str(round)+": Considering "+str(randX)+"x"+str(randY)+" of type "+self.map[randX][randY])
          if self.map[randX][randY]=="l":
            found = 1
            coords = {}
            coords['x'] = randX
            coords['y'] = randY
            self.cities.append(coords)


  def addCities(self):
    for city in self.cities:
      self.map[city['x']][city['y']] = "c"


  def printWorld(self):
    for y in range(1,self.height+1):
      for x in range(1,self.width+1):
        if self.map[x][y] == "c":
          print('\x1b[1;37;42m' + '*' + '\x1b[0m', end='')
        elif self.map[x][y] == "l":
          print('\x1b[1;37;42m' + ' ' + '\x1b[0m', end='')
        else:
          print('\x1b[1;37;44m' + ' ' + '\x1b[0m', end='')
      print("")
