with open("Day3\input.txt", "r") as f:
    lines = f.readlines()

#Part 1
numchars = len(lines[0]) +1
print(numchars)
mydata = list()
mydata.append(' '*numchars)
for line in lines:
    mydata.append(" "+line.strip().replace("."," ")+" ")
mydata.append(' '*numchars)

print(mydata[0])
print(mydata[1])
print(mydata[-2])
print(mydata[-1])

for data in mydata:
    print(len(data),end=" ")

def check_adjacent(row,col,mydata):
    checks = [[0,1],[0,-1],[1,1],[1,0],[1,-1],[-1,1],[-1,0],[-1,-1]]
    found = False
    for check in checks:
        cr = row + check[0]
        cc = col + check[1]
        tocheck = mydata[row+check[0]][col+check[1]]
        if not tocheck.isdigit():
            if tocheck != " ":
                return True
    return False

def check_adjacentgear(row,col,mydata):
    checks = [[0,1],[0,-1],[1,1],[1,0],[1,-1],[-1,1],[-1,0],[-1,-1]]
    found = False
    for check in checks:
        cr = row + check[0]
        cc = col + check[1]
        tocheck = mydata[row+check[0]][col+check[1]]
        if not tocheck.isdigit():
            if tocheck == "*":
                return True, row+check[0],col+check[1]
    return False,0,0



values = list()
for row in range(1,numchars-1): #[33,34,35,36,37]: 
    isnum = False;
    isadjacent = False;
    numstr= ""
    rowvalues = []
    for col in range(1,numchars):
        d = mydata[row][col]
        if d.isdigit():
            isnum = True
            numstr = numstr + d
        elif isnum==True:
            isnum=False
            if isadjacent==True:
                values.append(numstr)
                rowvalues.append(numstr)
                isadjacent = False
            numstr = ""
        else:
            numstr = ""
        if isnum:
            if check_adjacent(row,col,mydata):
                isadjacent = True
    print(rowvalues)
        #if col==1 or col==140: print(d, end = "")

p1sum = 0
for value in values:
    p1sum += int(value)

p2sum=0
# Find all potential gears!
asterisks = []
for row in range(1,numchars-1): #[33,34,35,36,37]: 
    for col in range(1,numchars):
        d = mydata[row][col]
        if d =="*":
            asterisks.append([row,col])
print(asterisks)

values = list()
geardict = {}
for row in range(1,numchars-1): #[33,34,35,36,37]: 
    isnum = False;
    isadjacent = False;
    numstr= ""
    adjgear=[0,0]
    rowvalues = []
    for col in range(1,numchars):
        d = mydata[row][col]
        if d.isdigit():
            isnum = True
            numstr = numstr + d
        elif isnum==True:
            isnum=False
            if isadjacent==True:
                values.append(numstr)
                rowvalues.append(numstr)
                isadjacent = False
                key = str(adjgear[0])+"-"+str(adjgear[1])
                if key in geardict:
                    geardict[key].append(numstr)
                else:
                    geardict[key] = [numstr]
                if len(geardict[key])>1: 
                    print(key, ">>>", geardict[key])
                    gearratio = int(geardict[key][0])*int(geardict[key][1])
                    p2sum += gearratio
                pass
            numstr = ""
        else:
            numstr = ""
        if isnum:
            val,r,c = check_adjacentgear(row,col,mydata)
            if val:
                isadjacent = True
                adjgear=[r,c]

    #print(rowvalues)
        #if col==1 or col==140: print(d, end = "")
print(geardict)


print("Part1:",p1sum, "Part2:",p2sum)