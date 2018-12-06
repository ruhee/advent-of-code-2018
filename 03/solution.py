#! /usr/local/bin/python3
with open('input.txt', 'r') as input:
  data = input.read().strip().split('\n')
  
  coords = {}
  
  # part 1
  for line in data:
    info, a, pos, dim = line.split(' ') # ['#id', '@', 'x,y:', 'dimxdim']
    x, y = pos.rstrip(':').split(',')
    width, height = dim.split('x')

    x = int(x)
    y = int(y)
    width = int(width)
    height = int(height)

    for x_val in range(x, x+width):
      for y_val in range(y, y+height):
        pt = str(x_val) + ',' + str(y_val)
        if pt in coords:
          coords[pt] += 1
        else:
          coords[pt] = 1

    def validate_claim(x, y, w, h):
      for x_val in range(x, x+w):
        for y_val in range(y, y+h):
          pt = str(x_val) + ',' + str(y_val)
          if coords[pt] > 1:
            return False
      return True

  items = {k:v for (k,v) in coords.items() if v >= 2}
  print(len(items))

  # at some point, perhaps I won't have to repeat all this...
  # but for now, part 2, quick and dirty
  for line in data:
    info, a, pos, dim = line.split(' ')
    x, y = pos.rstrip(':').split(',')
    width, height = dim.split('x')

    x = int(x)
    y = int(y)
    width = int(width)
    height = int(height)
    if validate_claim(x, y, width, height):
      print(info)