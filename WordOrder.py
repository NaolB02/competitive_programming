# Enter your code here. Read input from STDIN. Print output to STDOUT
hashmp = {}
n = int(input())
for i in range(n):
    word = input()
    if word not in hashmp:
        hashmp[word] = 1
    
    else:
        hashmp[word] += 1
        
print(len(hashmp))
for value in hashmp.values():
    print(value, end=" ")
