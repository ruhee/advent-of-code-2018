#! /usr/local/bin/python3
from operator import itemgetter

with open('input.txt', 'r') as input:
  data = input.read().strip().split('\n')

  bots = []
  for idx, el in enumerate(data):
    bots.append({
      'idx': idx, # do we need this? tbd
      'radius': int(el.split(', ')[1].strip('r=')),
      'coords': [int(i) for i in el.split(', ')[0].strip('pos=<>').split(',')]
    })

  bots = sorted(bots, key=itemgetter('radius'), reverse=True)
  top_bot = bots[0] # greatest signal radius

  bots_in_range = []

  def get_manhattan(coords):
    bot_coords = top_bot['coords']
    return abs(bot_coords[0] - coords[0]) + abs(bot_coords[1] - coords[1]) + abs(bot_coords[2] - coords[2])

  # get bots in range of strongest bot
  for idx, bot in enumerate(bots):
    if get_manhattan(bot['coords']) <= top_bot['radius']:
      bots_in_range.append(bot)

  print(len(bots_in_range))
