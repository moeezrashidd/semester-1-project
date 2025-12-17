rand = (144, 136,149,150,170,160)
roll = 115
N = roll % 10
if N == 0:
    N=1
newusers = rand[N-1::N]    
print(newusers)