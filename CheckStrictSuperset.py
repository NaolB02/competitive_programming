# Enter your code here. Read input from STDIN. Print output to STDOUT
A = set(map(int, input().split()))
n = int(input())
flag = True

for i in range(n):
    B = set(map(int, input().split()))
    
    if len(B - A) == 0 and len(A - B) > 0:
        continue

    else:
        flag = False
        print(flag)
        break

if flag:
    print(flag)
