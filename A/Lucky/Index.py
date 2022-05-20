def is_lucky(ticket):
    ans = ""

    firstHalfSum = 0
    endHalfSum = 0

    for i in range(len(ticket)):
        if i < 3:
            firstHalfSum += int(ticket[i])
        else:
            endHalfSum += int(ticket[i])

    if firstHalfSum == endHalfSum:
        ans = "YES"
    else: 
        ans = "NO"
    return ans

# Number of testcases
t = int(input())

for i in range(t):
    ticket = input()
    print(is_lucky(ticket))