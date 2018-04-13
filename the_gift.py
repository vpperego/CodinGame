import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
c = int(input())
budgets = []
for i in range(n):
    b = int(input())
    budgets.append(b)
 #[100, 1, 60] 
#print(c)
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
solution = []
if sum(budgets) < c:
    print("IMPOSSIBLE")
else:
    budgets = sorted(budgets)
    total = 0
    
    for b in range(n):
        value = int((c -total)/(n-b))
        if (value < budgets[b]):
            total += value
            solution.append(value)
        else:
            total += budgets[b]
            solution.append(budgets[b])
    
    for s in solution:
        print (s)
