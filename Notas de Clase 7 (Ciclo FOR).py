language = "P y t h o n"
for letter in language:
    print(letter)

numbers = [0, 1, 2, 3, 4, 5]
for number in numbers:
    print(number)

values = [2, 4, 6, 8, 10]
sum = 0
counter = 0
for value in values:
    counter += 1
    sum += value
average = sum/counter
print(f"The average is: {average}")

word = input("Enter a word: ")
vowels = 0
consonant = 0
for letter in word:
    if letter in "aeiou" or letter in "AEIOU":
        vowels += 1
    else:
        consonant += 1
    lenght = len(word)
print(f"The number of vowels is: {vowels}")
print(f"The number of consonants is: {consonant}")
print(f"The total of words is: {lenght}")
