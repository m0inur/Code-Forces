#                                                             C. Pair Programming
#                                                         time limit per test 2 seconds
#                                                         memory limit per test 512 megabytes
#                                                             input standard input
#                                                             output standard output

# Monocarp and Polycarp are learning new programming techniques. Now they decided to try pair programming.

# It's known that they have worked together on the same file for n+m minutes. Every minute exactly one of them made one change to the file. Before they started, there were already k lines written in the file.

# Every minute exactly one of them does one of two actions: adds a new line to the end of the file or changes one of its lines.

# Monocarp worked in total for n minutes and performed the sequence of actions [a1,a2,…,an]. If ai=0, then he adds a new line to the end of the file. If ai>0, then he changes the line with the number ai. Monocarp performed actions strictly in this order: a1, then a2, ..., an.

# Polycarp worked in total for m minutes and performed the sequence of actions [b1,b2,…,bm]. If bj=0, then he adds a new line to the end of the file. If bj>0, then he changes the line with the number bj. Polycarp performed actions strictly in this order: b1, then b2, ..., bm.

# Restore their common sequence of actions of length n+m such that all actions would be correct — there should be no changes to lines that do not yet exist. Keep in mind that in the common sequence Monocarp's actions should form the subsequence [a1,a2,…,an] and Polycarp's — subsequence [b1,b2,…,bm]. They can replace each other at the computer any number of times.

# Let's look at an example. Suppose k=3. Monocarp first changed the line with the number 2 and then added a new line (thus, n=2,a=[2,0]). Polycarp first added a new line and then changed the line with the number 5 (thus, m=2,b=[0,5]).

# Since the initial length of the file was 3, in order for Polycarp to change line number 5 two new lines must be added beforehand. Examples of correct sequences of changes, in this case, would be [0,2,0,5] and [2,0,0,5]. Changes [0,0,5,2] (wrong order of actions) and [0,5,2,0] (line 5 cannot be edited yet) are not correct.

# Input
# The first line contains an integer t (1≤t≤1000). Then t test cases follow. Before each test case, there is an empty line.

# Each test case contains three lines. The first line contains three integers k, n, m (0≤k≤100, 1≤n,m≤100) — the initial number of lines in file and lengths of Monocarp's and Polycarp's sequences of changes respectively.

# The second line contains n integers a1,a2,…,an (0≤ai≤300).

# The third line contains m integers b1,b2,…,bm (0≤bj≤300).

# Output
# For each test case print any correct common sequence of Monocarp's and Polycarp's actions of length n+m or -1 if such sequence doesn't exist.

# Example:

# Input:
# 5

# 3 2 2
# 2 0
# 0 5

# 4 3 2
# 2 0 5
# 0 6

# 0 2 2
# 1 0
# 2 3

# 5 4 4
# 6 0 8 0
# 0 7 0 9

# 5 4 1
# 8 7 8 0
# 0

# Output:
# 2 0 0 5 
# 0 2 0 6 5 
# -1
# 0 6 0 7 0 8 0 9
# -1

from pickle import TRUE

def pair_programming(lineCount, p1SeqLen, p2SeqLen, p1Sequence, p2Sequence):
    # keep track of lines count
    # if there is a line count we cannot reach
    # then its impossible so return -1
    p1SeqPointer = 0
    p2SeqPointer = 0
    ansStr = ""
    isCollectingZero = True

    # RULES
    # if uses for the current sequence action has been done, increase pointer
    # do this untill reaching the end of the sequence

    # while there are possible pointers for sequences
    while(p1SeqPointer < p1SeqLen or p2SeqPointer < p2SeqLen):
        # if there is a new line on current pointer
        # add it
        if p1SeqPointer < p1SeqLen:
            # if we are searching for a new line
            if p1Sequence[p1SeqPointer] == 0:
                ansStr += " 0"

                p1SeqPointer += 1
                lineCount += 1
            elif p1Sequence[p1SeqPointer] <= lineCount: 
                # if searching for a new line is done for seq i
                # if player 1 can complete his seq i
                ansStr += " " + str(p1Sequence[p1SeqPointer])
                p1SeqPointer += 1

        if p2SeqPointer < p2SeqLen:
            # if we are searching for a new line
            if p2Sequence[p2SeqPointer] == 0:
                ansStr += " 0"
                
                p2SeqPointer += 1
                lineCount += 1
            elif p2Sequence[p2SeqPointer] <= lineCount: 
                # if searching for a new line is done for seq i
                # if player 2 can complete his seq i
                ansStr += " " + str(p2Sequence[p2SeqPointer])
                p2SeqPointer += 1
        
        # if both the sequences are still in play
        # check if both is stuck 
        if p1SeqPointer < p1SeqLen and p2SeqPointer < p2SeqLen:
            if p1Sequence[p1SeqPointer] > lineCount and p2Sequence[p2SeqPointer] > lineCount:
                return "-1"
        # if the first player sequence still remain
        elif p1SeqPointer < p1SeqLen and p2SeqPointer >= p2SeqLen:
            if p1Sequence[p1SeqPointer] > lineCount:
                return "-1"
        # if the second player sequence still remain
        elif p2SeqPointer < p2SeqLen and p1SeqPointer >= p1SeqLen:
            if p2Sequence[p2SeqPointer] > lineCount:
                return "-1"

        ansStr = ansStr.strip()
        if isCollectingZero == True: isCollectingZero = False
        else: isCollectingZero = True

    return ansStr

# p1 - 2 0
# p2 - 0 5

# Number of testcases
n = int(input())

for i in range(n):
    input()
    lengths = input().split(" ")
    linesWritten = int(lengths[0])
    p1WorkedMins = int(lengths[1])
    p2WorkedMins = int(lengths[2])
    p1Sequence = list(map(int, input().split(" ")))
    p2Sequence = list(map(int, input().split(" ")))
    res = pair_programming(linesWritten, p1WorkedMins, p2WorkedMins, p1Sequence, p2Sequence)
    print(res)