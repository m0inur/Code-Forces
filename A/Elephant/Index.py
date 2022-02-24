n = int(input())
steps = 0
while (n > 0):
    if n >= 5:
        n -= 5
    elif n >= 4:
        n -= 4
    elif n >= 3:
        n -= 3
    elif n >= 2:
        n -= 2
    else: n -= 1
    steps += 1

print(steps)