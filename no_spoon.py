import sys
import math

# Don't let the machines win. You are humanity's last hope...
nodes = []
width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
for i in range(height):
    line = input()  # width characters, each either 0 or .
    for j in range (width):
        if line[j] == "0":
          nodes.append([j,i])  
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
#print (nodes[0])
for n in range(len(nodes)):
    rightFound = False
    downFound  = False
    x = nodes[n][0]
    y = nodes[n][1]
    for m in range(n+1,len(nodes)):
        if nodes[m][1] == y and rightFound == False:
            rightFound = True
            nodes[n].append(nodes[m][0])
            nodes[n].append(nodes[m][1])
            continue
        if nodes[m][0] == x:
            if rightFound == False:
                nodes[n].append(-1)
                nodes[n].append(-1)
                rightFound = True
            nodes[n].append(nodes[m][0])
            nodes[n].append(nodes[m][1])
            downFound = True
            break
    if rightFound == False:
                nodes[n].append(-1)
                nodes[n].append(-1)
    if downFound == False:
        nodes[n].append(-1)
        nodes[n].append(-1)

for n in nodes:
    for c in n:
        print (c,end =" ")
    print ()
# Three coordinates: a node, its right neighbor, its bottom neighbor
#print("0 0 1 0 0 1")
