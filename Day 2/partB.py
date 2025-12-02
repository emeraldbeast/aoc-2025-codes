s = input() 
L = s.split(',')
ans = 0
for x in L:
    A = x.split('-')
    l,r = int(A[0]),int(A[1]) 
    for j in range(l,r+1):
        y = str(j) 
        n = len(y) 
        state = False
        for k in range(1,n//2+1):
            if n%k:
                continue 
            z = n//k 
            val = y[:k]
            if val*z==y:
                state = True 
        if state:
            ans+=j
print(ans)