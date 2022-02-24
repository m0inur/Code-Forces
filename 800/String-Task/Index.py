# A. String Task
# time limit per test2 seconds
# memory limit per test256 megabytes
# input standard input
# output standard output
# Petya started to attend programming lessons. On the first lesson his task was to write a simple program. The program was supposed to do the following: in the given string, consisting if uppercase and lowercase Latin letters, it:

# deletes all the vowels,
# inserts a character "." before each consonant,
# replaces all uppercase consonants with corresponding lowercase ones.
# Vowels are letters "A", "O", "Y", "E", "U", "I", and the rest are consonants. The program's input is exactly one string, it should return the output as a single string, resulting after the program's processing the initial string.

# Help Petya cope with this easy task.

# Input
# The first line represents input string of Petya's program. This string only consists of uppercase and lowercase Latin letters and its length is from 1 to 100, inclusive.

# Output
# Print the resulting string. It is guaranteed that this string is not empty.

# Examples
# input
# tour

# output
# .t.r

# input
# Codeforces

# output
# .c.d.f.r.c.s

# input
# aBAcAba

# output
# .b.c.b

string = input()
ansStr = ""

for i in range(len(string)):
    ch = str.lower(string[i])
    # if current letter is a vowel then skip
    if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or ch == 'y'): continue
    ansStr += '.' + ch

print(ansStr)