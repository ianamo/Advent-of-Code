prac_fish = [3,4,3,1,2]

days = 18

def fsum(x, lim, diff=1):
  x+=diff
  if (x)<lim:
    return 1 + fsum(x,lim,7)+ fsum(x,lim,9)
  else:
    return 0


my_sum = len(fish)
for f in fish:
  my_sum+=fsum(f,258)
print (my_sum)