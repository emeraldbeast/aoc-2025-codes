try:
    ans = 0
    intervals = []
    while True:
        s = input()
        if s=="":
            intervals.sort()
            continue 
        if "-" in s:
            L = s.split("-") 
            l,r = int(L[0]),int(L[1])
            intervals.append((l,r))   
            continue 
        check = int(s)
        for x in intervals:
            l,r = x[0],x[1] 
            if l<=check<=r:
                ans+=1   
                break            
except:
    print(ans)