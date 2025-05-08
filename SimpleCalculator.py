print ("\nWelcome to the Calculator Program\n")

number_1 = float(input("Enter First Number: "))
number_2 = float(input("Enter Second Number: "))

print("\nChoose an operation\n" + "1. Addition\n" + "2. Subtraction\n" + "3. Multiplication\n" + "4. Division\n")
choice = int(input("Option: "))

if  (choice == 1) :
    print ("\nYour Total is", number_1 + number_2)

elif (choice == 2) :
    print ("\nYour Total is", number_1 - number_2)

elif (choice == 3) :
    print ("\nYour Total is", number_1 * number_2)

elif (choice == 4) :
    print ("\nYour Total is", number_1 / number_2)

else :
    print("\nYou have entered an invalid operation!")

print("\nThank you for Using This Program!!")