try:
    ans = 0 
    dial = 50 
    while True:
        s = input()
        direction,number = s[0],int(s[1:])
        if direction=="L":
            dial-=number 
            dial%=100 
        else:
            dial+=number 
            dial%=100 
        if dial==0:
            ans+=1 
except:
    print(ans)