try:
    ans = 0 
    ind = 0
    while True:
        s = input() 
        if ind==0:
            ind+=1 
            digits = ["" for _ in range(len(s))]
            for j in range(len(s)):
                if s[j] in "123456789":
                    digits[j] = s[j]
        elif s[0] not in "*+":
            for j in range(len(s)):
                if s[j] in "123456789":
                    digits[j]+=s[j]
        else:
            operators = s.split()
            ptr = 0
            mul,add=1,0
            for j in range(len(s)):
                if digits[j]=="":
                    ptr+=1
                    if add!=0:
                        ans+=add 
                        add = 0 
                    if mul!=1:
                        ans+=mul 
                        mul = 1 
                    continue
                elif operators[ptr]=="*":
                    mul*=int(digits[j])
                elif operators[ptr]=="+":
                    add+=int(digits[j])
            if mul!=1:
                ans+=mul 
            if add!=0:
                ans+=add
except:
    print(ans)