crabs = [16,1,2,0,4,2,7,1,2,14]

a = sum(crabs) // len(crabs)

def tot_dist (points, loc):
  d = 0
  for p in points:
    d+=(sum(range(abs(loc-p)+1)))
  return d

def find_min(points):
  avg = sum(points)//len(points)
  while (True):
    a = tot_dist(points,avg)
    b = tot_dist(points,avg+1)
    c = tot_dist(points,avg-1)
    print(a)
    if a < b and a < c:
      break
    if b<a:
      avg+=1
    else:
      avg-=1
  return a


print(find_min(real_crabs))