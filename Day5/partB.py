try:
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
except:
    merged = []
    for l,r in intervals:
        if not merged or merged[-1][1]<l-1:
            merged.append([l,r])
        else:
            merged[-1][1] = max(merged[-1][1],r)
    ans = 0
    for l,r in merged:
        ans+=r-l+1
    print(ans)
