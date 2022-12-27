# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
d = defaultdict(list)
n, m = input().split()
n = int(n)
m = int(m)

for index in range(n):
    letter = input()
    d[letter].append(str(index + 1))

for index in range(m):
    letter = input()
    
    if letter in d:
        print(' '.join(d[letter]))
    
    else:
        print(-1)
