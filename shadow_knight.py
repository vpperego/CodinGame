import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]
lX=0
rX=w-1
lY=0
rY=h-1
print ("w "+str(w),file=sys.stderr)
print ("h "+str(h),file=sys.stderr)

# game loop
while True:
   
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)


    if len(bomb_dir) == 1:
        if bomb_dir=='U':
            
            rY=y0-1
        elif bomb_dir=='D':
            lY=y0+1
        elif bomb_dir=='L':
            rX=x0-1
        else:
            lX=x0+1
    else:
        if bomb_dir=='UR':
            rY=y0-1
            lX=x0+1
        elif bomb_dir=='DR':
            lY=y0+1
            lX=x0+1
        elif bomb_dir=='UL':
            rY=y0-1
            rX=x0-1
        else:
            lY=y0+1
            rX=x0-1
            
    
    x0 = math.floor((lX+rX)/2)
    y0 = math.floor((lY+rY)/2)
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    
    # the location of the next window Batman should jump to.
    print(str(x0)+" "+str(y0))
    print ("lY "+str(lY),file=sys.stderr)
    print ("rY "+str(rY),file=sys.stderr)
