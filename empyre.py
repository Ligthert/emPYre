from map import Map

if __name__ == "__main__":
  map = Map(150,50)
  map.generateMap()
  map.findCoast()
  map.generateCities()
  map.addCities()
  map.printWorld()
