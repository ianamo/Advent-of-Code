num = [0] * 12
gamma = ['0']*12
epsilon = ['1']* 12

for l in data.split():
  for i, dig in enumerate(l):
    if dig == '1':
      num[i]+=1
    else:
        num[i]-=1

for i,n in enumerate(num):  
  if int(n)>0:
    gamma[i] = '1'
    epsilon[i] = '0'

g = int("".join(gamma), 2)
e = int("".join(epsilon), 2)

print (g*e)