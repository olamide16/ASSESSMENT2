word = input('Enter a word: ')
vowels = 0 
constants = 0
for i in word:
    if (i == 'a' or i == 'e' or i == 'i' or i == 'o'or i == 'u' or i == 'A'or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
        vowels = vowels + 1
    else:
        constants = constants + 1
print("The total number of Vowels in the word= ", vowels)
print("The total number of Cosonant in the word= ", constants)
    