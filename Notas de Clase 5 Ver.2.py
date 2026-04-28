number = int(input('Enter a number: '))
if number == 0:
    print('The number is zero')
    print('This is the end of the program')
else:
    if number > 0:
        if number % 2 == 0:
            print('The number is a positive and even')
        else:
            print('The number is a positive and odd')
    else:
        if number % 2 == 0:
            print('The number is a negative and even')
        else:
            print('The number is a negative and odd')
    print('This is the end of the program')
