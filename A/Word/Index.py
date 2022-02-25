# A. Word
# time limit per test 2 seconds
# memory limit per test 256 megabytes
# input standard input
# output standard output
# Vasya is very upset that many people on the Net mix uppercase and lowercase letters in one word. That's why he decided to invent an extension for his favorite browser that would change the letters' register in every word so that it either only consisted of lowercase letters or, vice versa, only of uppercase ones. At that as little as possible letters should be changed in the word. For example, the word HoUse must be replaced with house, and the word ViP — with VIP. If a word contains an equal number of uppercase and lowercase letters, you should replace all the letters with lowercase ones. For example, maTRIx should be replaced by matrix. Your task is to use the given method on one given word.

# Input
# The first line contains a word s — it consists of uppercase and lowercase Latin letters and possesses the length from 1 to 100.

# Output
# Print the corrected word s. If the given word s has strictly more uppercase letters, make the word written in the uppercase register, otherwise - in the lowercase one.

# Examples
# input
# HoUse

# output
# house

# input
# ViP

# output
# VIP

# input
# maTRIx

# output
# matrix

word = input()
lowerCaseCount = 0
upperCaseCount = 0

for i in range(len(word)):
    if word[i] == word[i].upper():
        upperCaseCount += 1
    else: 
        lowerCaseCount += 1

if upperCaseCount == lowerCaseCount:
    print(word.lower())
elif upperCaseCount > lowerCaseCount:
    print(word.upper())
else: 
    print(word.lower())