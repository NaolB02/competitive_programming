# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int, input().split())
H = list(input().split())
A = set(input().split())
B = set(input().split())
happiness = 0

for element in H:
    if element in A:
        happiness += 1
    elif element in B:
        happiness -= 1

print(happiness)
