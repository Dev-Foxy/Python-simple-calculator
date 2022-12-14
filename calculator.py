# First we need to add four function for addition,substraction,multipication and division
def addition(a,b):
    answer = a+ b
    print(str(a) + "+ " + str(b) + "= " + str(answer))
def substraction(a,b):
    answer = a- b
    print(str(a) + "- " + str(b) + "= " + str(answer))
def multipication(a,b):
    answer = a* b
    print(str(a) + "* " + str(b) + "= " + str(answer))
def division(a,b):
    answer = a/ b
    print(str(a) + "/ " + str(b) + "= " + str(answer))

# Now we need to take choice for the function

while True:
    print("Enter A for addition")
    print("Enter B for substraction")
    print("Enter C for multipication")
    print("Enter D for division")
    print("Enter E for exit")

    choice = input("Enter your choice: ")

    if choice == "a" or choice == "A":
        a = int(input("Enter first number: "))
        b= int(input("Enter second number: "))
        addition(a,b)
    elif choice == "b" or choice == "B":
        a = int(input("Enter first number: "))
        b= int(input("Enter second number: "))
        substraction(a,b)
    elif choice == "c" or choice == "C":
        a = int(input("Enter first number: "))
        b= int(input("Enter second number: "))
        multipication(a,b)
    elif choice == "d" or choice == "D":
        a = int(input("Enter first number: "))
        b= int(input("Enter second number: "))
        division(a,b)
    else:
        print("Program finished")
        quit()