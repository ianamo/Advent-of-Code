data = """2199943210
3987894921
9856789892
8767896789
9899965678"""

lines = real_data.split("\n")
centers = []
y = 0

while y<len(lines):
    x = 0
    while x <len(lines[y]):
        curr = int(lines[y][x])
        if y+1<len(lines): down = int(lines[y+1][x])
        else: down = None
        if y-1>=0: up = int(lines[y-1][x])
        else: up = None
        if x+1<len(lines[y]): right = int(lines[y][x+1])
        else: right = None
        if x-1>=0: left = int(lines[y][x-1])
        else: left = None

        dirs = [d for d in (up,down,right,left) if d is not None]

        if any([d<=curr for d in dirs]):
            x+=1
            continue
        else:
            centers.append((y,x))
            x+=1
    y+=1
    #print(y)

def find_basin(coord,data,path=[]):
    y = coord[0]
    x = coord[1]
    if y+1<len(data) and int(data[y+1][x])<9 and ((y+1),x) not in path:
        #print ("at coord",y+1,x)
        #print("the value is",data[y+1][x])
        path.append(((y+1),x))
        path += find_basin(((y+1),x),data,path)
    if y-1>=0 and int(data[y-1][x])<9 and ((y-1),x) not in path:
        #print ("at coord",y-1,x)
        #print("the value is",data[y-1][x])
        path.append(((y-1),x))
        path+=find_basin(((y-1),x),data,path)
    if x+1<len(data[y]) and int(data[y][x+1])<9 and (y,(x+1)) not in path:
        #print ("at coord",y,x+1)
        #print("the value is",data[y][x+1])
        path.append(((y),x+1))
        path+=find_basin((y,x+1),data,path)
    if x-1>=0 and int(data[y][x-1])<9 and (y,(x-1)) not in path:
        #print ("at coord",y,x-1)
        #print("the value is",data[y][x-1])
        path.append((y,x-1))
        path+=find_basin((y,x-1),data,path)
    path = list(dict.fromkeys(path))
    return path
    

basins = []
for c in centers:
    basins.append(len(find_basin(c,lines,[])))

basins = sorted(basins)
print(basins[-1]*basins[-2]*basins[-3])
