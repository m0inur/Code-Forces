# Number of testcases
t = int(input())
lowercaseLetters = "abcdefghijklmnopqrstuvwxyz"

for i in range(t):
    num = 0
    s = input()
    n = -1

    for i in range(26):
        for j in range(0, 26):
            if(i != j):
                num += 1
                if(lowercaseLetters[i] + lowercaseLetters[j] == s):
                    n = num
                    break
        
        if n != -1:
            break

    print(n)