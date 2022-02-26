# A. Chat room
# time limit per test 1 second
# memory limit per test 256 megabytes
# input standard input
# output standard output
# Vasya has recently learned to type and log on to the Internet. He immediately entered a chat room and decided to say hello to everybody. Vasya typed the word s. It is considered that Vasya managed to say hello if several letters can be deleted from the typed word so that it resulted in the word "hello". For example, if Vasya types the word "ahhellllloou", it will be considered that he said hello, and if he types "hlelo", it will be considered that Vasya got misunderstood and he didn't manage to say hello. Determine whether Vasya managed to say hello by the given word s.

# Input
# The first and only line contains the word s, which Vasya typed. This word consisits of small Latin letters, its length is no less that 1 and no more than 100 letters.

# Output
# If Vasya managed to say hello, print "YES", otherwise print "NO".

# Examples
# input
# ahhellllloou 

# output
# YES  

# input
# hlelo

# output
# NO

s = input().upper()


hasFoundH = False
hasFoundE = False
hasFoundL1 = False
hasFoundL2 = False
hasFoundO = False

for i in range(len(s)):
    if hasFoundH == False:
        if s[i] == 'H': hasFoundH = True
    elif hasFoundE == False:
        if s[i] == 'E': hasFoundE = True
    elif hasFoundL1 == False:
        if s[i] == 'L': hasFoundL1 = True
    elif hasFoundL2 == False:
        if s[i] == 'L': hasFoundL2 = True    
    elif hasFoundO == False:
        if s[i] == 'O': hasFoundO = True

if hasFoundH and hasFoundE and hasFoundL1 and hasFoundL2 and hasFoundO: print("YES") 
else: print("NO")