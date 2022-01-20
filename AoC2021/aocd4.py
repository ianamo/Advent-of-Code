prac_nums = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]

prac_boards = """22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""

boards = data_boards.split("\n\n")
marked = {} # hash reference for all marked spaces

def check_board(board, n):
  """
  Given a bingo board and a number to check, return None if not found or the coordinates if it is found.
  """
  for l, nums in enumerate(board.split("\n")):
    nm = nums.split()
    if n in nm:
      return l, nm.index(n) # coordinates to store in reference hash
  return None   

def bingo(coords):
  """
  Examine a set of 5x5 grid coordinates for whether they contain a bingo. If they do, return whether the bingo occured in a row or column and which one (useful sanity check). Otherwise, return None.
  """
  for row in range(5):
    m = 0
    for column in range(5):
      if (row, column) in coords:
        m +=1
    if m >4:
      return ('row', row)
  for column in range(5):
    m = 0
    for row in range(5):
      if (row, column) in coords:
        m +=1
    if m >4:
      return ('column', column)
  return None

bingo_boards=[] # This will contain all boards with bingos. The last one added is the one we're after.
bing=0 # variable to break out of for loop
for n in bingo_nums:
  if bing>0:
    break
  for i, b in enumerate(boards):
    coord = check_board(b,str(n)) #try to get coords of any marked spaces...
    if coord is not None:
      if i in marked.keys():
        marked[i].append(coord) # ... and store them in reference hash 
      else:
        marked[i] = [coord]
    if i in marked.keys():
      winner = bingo(marked[i]) #check for bingos
      if winner is not None and i not in bingo_boards:
        bingo_boards.append(i)
        if len(bingo_boards)==len(boards): # is this last board to bingo?
          win_num = n
          bing += 1
          break

# now add up all unmarked spaces in winning board
unmarked_sum = 0    
for l_num, l in enumerate(boards[bingo_boards[-1]].split("\n")):
  for n_num, num in enumerate(l.split()):
    if (l_num, n_num) not in marked[bingo_boards[-1]]:
      unmarked_sum += int(num)

print (unmarked_sum * win_num)