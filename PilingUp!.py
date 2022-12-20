# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
for i in range(T):
    n = int(input())
    blocks = list(map(int, input().split()))
    curblock = float('inf')
    s, e = 0 , len(blocks) - 1
    
    while e > s:
        blockleft = blocks[s]
        blockright = blocks[e]
        if blockleft >= blockright and blockleft <= curblock:
            s += 1
            curblock = blockleft
        elif blockleft < blockright and blockright <= curblock:
            e -= 1
            curblock = blockright
        
        else:
            print("No")
            break
    
    if s == e:
        print("Yes")
