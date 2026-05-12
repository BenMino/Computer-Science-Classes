language = 'Python'
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