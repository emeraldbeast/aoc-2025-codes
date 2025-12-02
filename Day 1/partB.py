try:
    ans = 0 
    dial = 50 
    while True:
        s = input()
        direction,number = s[0],int(s[1:])
        for _ in range(number): #Checking through each state one by one
            if direction=="L":
                dial-=1 
                dial%=100 
            else:
                dial+=1 
                dial%=100 
            if dial==0:
                ans+=1 
except:
    print(ans)