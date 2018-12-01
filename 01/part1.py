#! /usr/bin/python
with open('input.txt', 'r') as input:
  data = input.read().strip().split('\n')

  sum = 0
  i = 0
  while i < len(data):
    sum += int(data[i])
    i += 1
    
  print sum
  