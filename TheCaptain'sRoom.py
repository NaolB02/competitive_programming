# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
k = int(input())
rooms = list(input().split())
roomNum = Counter(rooms)

for room in roomNum:
    if roomNum[room] == 1:
        print(room)
