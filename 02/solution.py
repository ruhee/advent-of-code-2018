#! /usr/bin/python
from collections import Counter

def diff(a, b):
    diffIndexes = []
    for i, x in enumerate(a):
      if x != b[i]:
        diffIndexes.append(i)
    return diffIndexes

def sliced(string, idx):
  return string[:(idx)] + string[(idx+1):]

with open('input.txt', 'r') as input:
  data = input.read().strip().split('\n')

  # part 1
  twos = []
  threes = []

  for idx, el in enumerate(data):
    counter = Counter(el)
    three_exists = [key for (key, val) in counter.items() if val == 3]
    two_exists = [key for (key, val) in counter.items() if val == 2]
    if three_exists:
      threes.append(el)
    if two_exists:
      twos.append(el)

  print len(threes) * len(twos)


  # part 2
  possibles = []

  for idx, el in enumerate(data):
    for i, item in enumerate(data):
      intersect = Counter(el) & Counter(item)
      length = len(''.join(intersect.elements()))
      if length == len(el) - 1:
        if el not in possibles:
          possibles.append(el)
        if item not in possibles:
          possibles.append(item)

  matches = []
  for idx, el in enumerate(possibles):
    for i, item in enumerate(possibles):
      if i != idx:
        diff_idx = diff(el, item)
        if len(diff_idx) == 1:
          print sliced(el, diff_idx[0])
          # this prints the answer twice, whatever, yolo
