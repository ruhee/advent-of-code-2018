#! /usr/local/bin/python3
with open('input.txt', 'r') as input:
  data = sorted(input.read().strip().split('\n'))

  current_guard: None
  sleeps = {}

  for i, line in enumerate(data):
    timestamp, instruction = line.split("] ")
    if instruction.startswith("Guard #"):
      current_guard = instruction.lstrip("Guard #").rstrip(" begins shift")
      if current_guard not in sleeps:
        sleeps[current_guard] = {}
    else:
      # it's not a guard so this is a sleep/wake situation
      if instruction.startswith("falls asleep"):
        start_min = int(timestamp.split(" ")[1].split(":")[1])
        end_min = int(data[i+1].split("] ")[0].split(" ")[1].split(":")[1]) # this assumes the line after "falls asleep" is always "wakes up". true?
        for x in range(start_min, end_min):
          if x in sleeps[current_guard]:
            sleeps[current_guard][x] += 1
          else:
            sleeps[current_guard][x] = 1
  
  # now get the total minutes each guard was sleeping
  guard_totals = {}
  for k, v in sleeps.items():
    guard_totals[k] = sum(v.values())

  sleepy_guard = max(guard_totals.items(), key=lambda k: k[1])[0] # ('10', 50)
  sleep_minutes = max(sleeps[sleepy_guard].items(), key=lambda k: k[1])[0]
  print("guard", sleepy_guard, "sleeps", sleep_minutes, "total", int(sleepy_guard) * int(sleep_minutes))

  # part 2
  guard = ''
  minute = 0
  max_sleeps = 0
  for k, v in sleeps.items():
    if len(v.items()) > 0:
      current_max = max(v.items(), key=lambda k: k[1])[1]
      if current_max > max_sleeps:
        max_sleeps = current_max
        guard = k
        minute = max(v.items(), key=lambda k: k[1])[0]
  
  print(guard, minute, int(guard) * int(minute))