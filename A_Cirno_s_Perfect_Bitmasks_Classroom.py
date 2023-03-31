t = int(input())

for _ in range(t):
    x = int(input())
    copy_x = x
    y = 0
    i = 0

    while 1 & copy_x != 1:
        i += 1
        copy_x >>= 1
    
    y |= (1 << i)

    if x ^ y and x & y:
        print(y)
        continue
    
    copy_x = x
    i = 0
    while 1 & copy_x != 0:
        i += 1
        copy_x >>= 1
    
    y |= (1 << i)
    print(y)
    
