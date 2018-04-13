import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
class Node:
	
	def __init__(self,key):
		self.child = []
		self.k = key
		
	def searchChilds(self,key):
		for node in self.child:
			if node.k == key:
				return node
		return None

def insert(root,string):
    node = root
    i = 0
    n = len(string)
    while(i < n):
        searchResult = node.searchChilds(string[i])
        if searchResult !=None:
            node = searchResult
            i = i + 1
        else:
            break
    
    while( i < n):
        newNode = Node(string[i])
        node.child.append(newNode)
        node = newNode
        i = i+ 1

def printChilds(node):
    for child in node.child:
        print (child.k, file=sys.stderr)

def getSize(root):
    total = len(root.child)
    for node in root.child:
        total = total + getSize(node)
    return total
        
n = int(input())
r = Node('a')
for i in range(n):
    telephone = input()
#    if telephone[0] not in r:
#        node = Node(telephone[0])
#        r.append
#    print (telephone[0])    
    insert(r,telephone)
    
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

#printChilds(r)
#print (r.child,file=sys.stderr)

# The number of elements (referencing a number) stored in the structure.
print(str(getSize(r) ))
