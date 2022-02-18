# A. Way Too Long Words
# time limit per test: 1 second
# memory limit per test: 256 megabytes
# input: standard input
# output: standard output
# Sometimes some words like "localization" or "internationalization" are so long that writing them many times in one text is quite tiresome.

# Let's consider a word too long, if its length is strictly more than 10 characters. All too long words should be replaced with a special abbreviation.

# This abbreviation is made like this: we write down the first and the last letter of a word and between them we write the number of letters between the first and the last letters. That number is in decimal system and doesn't contain any leading zeroes.

# Thus, "localization" will be spelt as "l10n", and "internationalization» will be spelt as "i18n".

# You are suggested to automatize the process of changing the words with abbreviations. At that all too long words should be replaced by the abbreviation and the words that are not too long should not undergo any changes.

# Input
# The first line contains an integer n (1 ≤ n ≤ 100). Each of the following n lines contains one word. All the words consist of lowercase Latin letters and possess the lengths of from 1 to 100 characters.

# Output
# Print n lines. The i-th line should contain the result of replacing of the i-th word from the input data.

# Examples
# input
# 4
# word
# localization
# internationalization
# pneumonoultramicroscopicsilicovolcanoconiosis

# output
# word
# l10n
# i18n
# p43s

def get_abbreviation_of_word(word):
    n = len(word)
    if n <= 10: return word
    return word[0] + "" + str(n - 2) + "" + word[n - 1]

# Number of testcases
n = int(input())

for i in range(n):
    word = input()
    print(get_abbreviation_of_word(word))