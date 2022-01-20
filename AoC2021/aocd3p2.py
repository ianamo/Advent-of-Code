
practice_data = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""

def bin_sort (nums, i, r=0):
  count = 0
  left = []
  right = []
  
  if len (nums)==1:
    return nums
  for n in nums:
    if n[i] == '1':
      count += 1
      left.append(n)
    else:
      count -= 1
      right.append(n)
  if r ==1:
    count *=-1
  if count >0 or (count==0 and r==0):
    nums = bin_sort(left, i+1,r)
  else:
    nums = bin_sort(right,i+1,r)
  return nums

gamma = bin_sort(data.split(), 0)
epsilon = bin_sort(data.split(), 0, 1)

#gamma = bin_sort(practice_data.split(), 0)
#epsilon = bin_sort(practice_data.split(), 0, 1)

g = int(gamma[0], 2)
e = int(epsilon[0], 2)

print (gamma[0])
print(epsilon[0])
print (g*e)