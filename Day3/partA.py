try:
    ans = 0
    while True:
        k = 2 # You can change this to k = 12 to get answer for first part
        s = input()
        n = len(s)
        L = []
        remove = n-k 
        for ch in s:
            d = int(ch)
            while L and remove>0 and int(L[-1])<d:
                L.pop()
                remove -= 1
            L.append(str(d))
        L = L[:k]
        res = "".join(L)
        ans+=int(res)
except EOFError:
    print(ans)