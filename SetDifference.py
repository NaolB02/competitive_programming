# Enter your code here. Read input from STDIN. Print output to STDOUT
nEnglish = int(input())
english = set(map(int, input().split()))
nFrench = int(input())
french = set(map(int, input().split()))

franco_english = english - french
print(len(franco_english))
