#! /usr/local/bin/python3

def find_completable(steps, completed):
  items = []
  for step in steps:
    if step not in completed:
      if set(steps[step]).issubset(set(completed)) or len(steps[step]) == 0:
        items.append(step)
  return sorted(items)[0]

with open('input.txt', 'r') as input:
  data = input.read().strip().split('\n')

  steps = {}
  all_steps = []

  for line in data: 
    # look, I should have used a regex, but I didn't
    prerequisite, step = line[5:][:32].split(" must be finished before step ")
    
    if step in steps:
      steps[step].append(prerequisite)
    else:
      steps[step] = [prerequisite]
    all_steps.append(step)
    all_steps.append(prerequisite)

  unique_steps = set(all_steps)
  completed = []

  # add the items that have no prerequisites
  for item in unique_steps:
    if item not in steps:
      steps[item] = []

  while len(completed) < len(unique_steps):
    completed.append(find_completable(steps, completed))

  print(''.join(completed))
