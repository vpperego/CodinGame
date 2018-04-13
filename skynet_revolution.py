import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
n, l, e = [int(i) for i in input().split()]

vizinhos =[]
for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    vizinhos.append([n1,n2])

gateways = []
for i in range(e):
    ei = int(input())  # the index of a gateway node
    gateways.append(ei)
    
# game loop
visiteds = []
while True:
    si = int(input())  # The index of the node on which the Skynet agent is positioned this turn
    visiteds.append(si)
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    print (n, file=sys.stderr)
    closestGateway  = max(gateways)
    
    destroyed = False
    for i,j in vizinhos:
        if i==si and j in gateways:
            destroyed = True
            print(str(si) + " " + str(j))
            break
        elif j ==si and i in gateways:
            destroyed = True
            print(str(si) + " " + str(i))
            break
    if destroyed == False:
        for i,j in vizinhos:    
            if i==si and j not in visiteds:
                print(str(si) + " " + str(j))
                break
            elif j ==si and i not in visiteds:
                print(str(si) + " " + str(i))
                break
