# show menu
print("Select an operation")
print("1.Add")
print("2.Subtract")
print("3.Divide")
print("4.Multiply")

# take input from user
selection =input("Select (1/2/3/4): ")

number1 =int(input("number1: "))
number2 = int(input("number2: "))


if selection == '1':
    print(number1, "+", number2, "=", number1+number2)
elif selection == '2':
    print(number1, "-", number2, "=", number1-number2)
elif selection == '3':
    print(number1, "/", number2, "=", number1/number2)
elif selection == '4':
    print(number1, "*", number2, "=", number1*number2)
else:
    print("invalid input")
