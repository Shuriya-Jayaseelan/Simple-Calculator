print ("\nWelcome to the Calculator Program\n")

number_1 = float(input("Enter First Number: "))
number_2 = float(input("Enter Second Number: "))

print("\nChoose an operation\n" + "1. Addition\n" + "2. Subtraction\n" + "3. Multiplication\n" + "4. Division\n")
choice = int(input("Option: "))
result = 0

if choice == 1:
    result = number_1 + number_2

elif choice == 2:
    result = number_1 - number_2

elif choice == 3:
    result = number_1 * number_2

elif choice == 4:
    if number_2 == 0:
        print("Cannot Divide By Zero!")
        exit()
    result = number_1 / number_2

else :
    print("\nYou have chosen an invalid option! Please try again later!")

print("\nThe Result is {r:1.3}".format(r = result))

print("\nThank you for Using This Program!!")