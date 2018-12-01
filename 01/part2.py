#! /usr/bin/python
import itertools

with open('input.txt', 'r') as input:
  data = input.read().strip().split('\n')
  sum = 0
  frequencies = []

  for el in itertools.cycle(data):
    sum += int(el)

    if sum in frequencies:
      print sum
      break
    else:
      frequencies.append(sum)    
      