try:
    grid = []
    while True:
        s = input()
        grid.append(list(s))
except:
    n = len(grid)
    m = len(grid[0])
    final = 0
    while True:
        ans = 0
        pos = []
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==".":continue
                neighbours = 0 
                if r-1>=0 and grid[r-1][c]=="@":
                    neighbours+=1 
                if r+1<n and grid[r+1][c]=="@":
                    neighbours+=1 
                if c-1>=0 and grid[r][c-1]=="@":
                    neighbours+=1 
                if c+1<m and grid[r][c+1]=="@":
                    neighbours+=1 
                if r-1>=0 and c-1>=0 and grid[r-1][c-1]=="@":
                    neighbours+=1 
                if r-1>=0 and c+1<m and grid[r-1][c+1]=="@":
                    neighbours+=1 
                if r+1<n and c-1>=0 and grid[r+1][c-1]=="@":
                    neighbours+=1 
                if r+1<n and c+1<m and grid[r+1][c+1]=="@":
                    neighbours+=1 
                if neighbours<4:
                    ans+=1 
                    pos.append((r,c))
        for x in pos:
            r,c = x[0],x[1]
            grid[r][c]="."
        final+=ans 
        if ans==0:
            break 
    print(final)