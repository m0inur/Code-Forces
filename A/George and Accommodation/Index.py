n = int(input())
possibleRoomCount = 0

for i in range(n):
    room = input().split(" ")
    p = int(room[0])
    q = int(room[1])

    if p + 2 <= q:
        possibleRoomCount += 1

print(possibleRoomCount)