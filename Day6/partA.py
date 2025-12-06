try:
    ind = 0 
    while True:
        s = input()
        nums = s.split()
        if ind==0:
            n = len(nums) 
            ind+=1
            numbers = [[] for _ in range(n)]
            for j in range(n):
                numbers[j] = [int(nums[j])]
        elif nums[0] in "*+":
            n = len(nums)
            ans = 0
            for j in range(n):
                if nums[j]=="*":
                    mul = 1
                    for k in numbers[j]:
                        mul*=k 
                    ans+=mul 
                else:
                    add = 0
                    for k in numbers[j]:
                        add+=k 
                    ans+=add
        else:
            n = len(nums)
            for j in range(n):
                numbers[j].append(int(nums[j]))
except:
    print(ans)