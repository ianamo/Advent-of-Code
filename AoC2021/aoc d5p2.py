import re

prac_input = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""

def parse_line (line):
  pattern = '(\d+),(\d+) \-> (\d+),(\d+)'
  m = re.match(pattern, line)
  return (int(m[1]), int(m[2]), int(m[3]), int(m[4]))

def draw_line(x1, y1, x2, y2):
  coords = []
  if x1 == x2:
    if y1>y2:
      y1, y2 = y2, y1
    coords.append((x1, y1))
    for n in range ((y1+1), (y2+1)):
      coords.append((x1, n))
    return coords
  elif y1 == y2:
    if x1>x2:
      x1, x2 = x2, x1
    coords.append((x1, y1))
    for n in range ((x1+1), (x2+1)):
      coords.append((n, y1))
    return coords
  elif x1 == y1:
    if x1>x2:
      x1, x2 = x2, x1
      y1,y2 = y2, y1
    for n in range (x1, (x2+1)):
      coords.append((n, n))
    return coords
  elif x1 == y2 or x2 == y1:
    if x1>x2:
      x1, x2 = x2, x1
      y1,y2 = y2, y1
    for n in range ((x2-x1)+1):
      coords.append(((x1+n), (x2-n)))
    return coords

coord_num = {}

for l in data.split("\n"):
  coord = draw_line(*parse_line(l))
  if coord is not None:
    for c in coord:
      if c not in coord_num.keys():
        coord_num[c] = 1
      else:
        coord_num[c] += 1

count = 0

for v in coord_num.values():
  if v > 1:
    count += 1

print(count)