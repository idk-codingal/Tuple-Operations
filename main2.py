def palind(level):
    e = len(level) - 1
    s = 0
    while(s < e):
        if(level[s]!= level[e]):
            return False
        s+= 1
        e-= 1
    return True
r = (1,2,3 ,3,2,1,)
if palind(r):
    print("The Tuple is a flipflop")
else:
    print("The Tuple is not flipflop")