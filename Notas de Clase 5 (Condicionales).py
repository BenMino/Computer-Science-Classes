a = int(input('Enter a grade over 100: '))
if a >= 90 and a <= 100:
    print(f'{a} is equal to A')
else:
    if a >= 80 and a <= 89:
        print(f'{a} is equal to B')
    else:
        if a >= 70 and a <= 79:
            print(f'{a} is equal to C')
        else:
            if a >= 60 and a <= 69:
                print(f'{a} is equal to D')
            else:
                print(f'{a} is equal to F')
print('This is the end of the program')