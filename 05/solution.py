#! /usr/local/bin/python3

def react(input):
  for idx, char in enumerate(input):
    if idx < len(input) - 1: # whoops
      next_char = input[idx+1]
      if (char.lower() == next_char.lower() and
        char != next_char):
        return input[:idx] + input[(idx+2):]
  return input

with open('input.txt', 'r') as input:
  data = input.read().strip().rstrip('\n')

  test_input = 'dabAcCaCBAcCcaDA'

  init_input = data
  # complete = False

  # while not complete:
  #   count = len(init_input)
  #   init_input = react(init_input)

  #   if count == len(init_input):
  #     complete = True
  #     print(len(init_input))

  # part 2
  reacted = {}
  for alpha in 'abcdefghijklmopqrstuvwxyz':
    stripped = init_input.replace(alpha, '').replace(alpha.upper(), '')

    complete = False

    while not complete:
      count = len(stripped)
      stripped = react(stripped)

      if count == len(stripped):
        complete = True
        reacted[alpha] = len(stripped)
        print(alpha, len(stripped))
  print(reacted)