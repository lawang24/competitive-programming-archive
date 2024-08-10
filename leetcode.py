def minFlips(grid) -> int:
    
    # find non-middle ones

    m, n = len(grid), len(grid[0])
    ans = 0

    # pure even cases
    for row_idx in range(m//2):
        i = 0
        j = n-1
        while i<j:
            count = grid[row_idx][i]+grid[row_idx][j]+grid[m-1-row_idx][i]+grid[m-1-row_idx][j]
            ans+=min(count, 4-count)
            i+=1
            j-=1

    # cross handler
    cross_values = 0
    avail_cross = 0
    if m%2 == 1:
        avail_cross+=n
        row = m//2+1
        for col in range(n):
            cross_values+=grid[row][col]
    
    # cross handler
    if n%2 == 1:
        avail_cross+=m
        col = n//2+1
        for row in range(m):
            cross_values += grid[row][col]

    if n%2 == 1 and m%2 == 1:
        avail_cross-=2
        cross_values-=1
        ans+=1

    extra = 0
    mod = cross_values%4
    if 4-(mod)+cross_values<=avail_cross:
        extra = min(4-mod, mod)
    else:
        extra =mod

    ans+= extra

    return ans
        
grid = [[1,0,0],[0,1,0],[0,0,1]]

print(minFlips(grid))