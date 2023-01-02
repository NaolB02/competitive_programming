from collections import defaultdict
n = int(input())

for _ in range(n):
    length = int(input())
    a = list(map(int, input().split()))
    s = input()

    mappings = {}
    yes = True

    for index, number in enumerate(a):
        if number in mappings:
            if mappings[number] != s[index]:
                yes = False
                print("NO")
                break
        
        else:
            mappings[number] = s[index]

    if yes:
        print("YES")
