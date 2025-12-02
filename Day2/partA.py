s = input() 
L = s.split(',') 
ans = 0
for x in L:
    A = x.split('-') 
    l,r = int(A[0]),int(A[1]) 
    for j in range(l,r+1):
        y = str(j) 
        n = len(y) 
        if n%2:
            continue 
        if y[:n//2]==y[n//2:]:
            ans+=j 
print(ans)