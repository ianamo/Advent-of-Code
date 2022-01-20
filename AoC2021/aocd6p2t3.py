from math import factorial

prac_fish = [3,4,3,1,2]

def fsearch(f, d):
  f+=1
  if f>=d :
    return 1
  i = (d-f)//9
  j = (d-f)//7
  tot=1
  for n in range(i+1):
    tot += 2**n
  while j>i:
    for r,n in enumerate(range(((7*j)+f),((9*j)+f),2)):
      if n<=d:
        tot+=(factorial(j) / (factorial(j-r)*factorial(r)))
    j-=1
  return tot

days = 256
fnums = {}      
my_sum = 0
for f in fish:
  if f not in fnums.keys():
    fnums[f] = fsearch(f,days)
    my_sum+=fnums[f]
  else:
    my_sum+=fnums[f]
print (my_sum)

#def ftest(f, d, func=fsearch):  
#  for n in range(d+1):
#    tot=0
#    for fsh in f:
#      tot += func(fsh,n)
#    print(tot)
#  return tot

#ftest(fish,80)