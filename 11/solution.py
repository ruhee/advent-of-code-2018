#! /usr/local/bin/python3
serial = 8141
grid_size = 300

grid = [[0 for y in range(grid_size)] for x in range(grid_size)]

# [
#   [0,1,2,3,4], # x0
#   [5,6,7,8,9], # x1
# ]
#
# grid[x][y]


# build grid
for x in range(grid_size):
  for y in range(grid_size):
    rack_id = x + 10
    power_level = rack_id * y + serial
    power_level = power_level * rack_id
    power_level = int(str(power_level)[-3:][0])
    power_level -= 5
    grid[x][y] = power_level

def sum_square(x, y):
  if x+2 < grid_size and y+2 < grid_size:
    return (
      grid[x][y] +
      grid[x][y+1] +
      grid[x][y+2] +
      grid[x+1][y] +
      grid[x+1][y+1] +
      grid[x+1][y+2] +
      grid[x+2][y] +
      grid[x+2][y+1] +
      grid[x+2][y+2]
    )
  else:
    return 0

# start calculating
highest_coords = ''
square_val = 0

for x, row in enumerate(grid):
  for y, value in enumerate(row):
    current_sum = sum_square(x, y)
    if current_sum > square_val:
      square_val = current_sum
      highest_coords = str(x) + ',' + str(y)

print(highest_coords)
