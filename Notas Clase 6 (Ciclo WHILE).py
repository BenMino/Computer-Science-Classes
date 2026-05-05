option = " "

while option != "c":
    print("--MENU--")
    print("A). Salute")
    print("B). Show Message")
    print("C). Exit")
    
    option = input("Select an option: ")

    if option == "a":
        print("Welcome!")
    elif option == "b":
        print("We are learning WHILE loops.")
    elif option == "c":
        print("Exiting the program.")
    else:
        print("Invalid option, please try again.")