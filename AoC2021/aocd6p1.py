
fish = [3,4,3, 1,2]

for n in range(30):
  i=0
  l = len(fish)
  print(l)
  while i < l:
    if fish[i] ==0:
      fish[i] = 6
      fish.append(8)
    else:
      fish[i]-=1
    i+=1
