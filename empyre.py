from map import Map

if __name__ == "__main__":
  map = Map()
  map.generateMap()
  map.findCoast()
  map.generateCities()
  map.addCities()
  map.printWorld()
