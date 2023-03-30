class Calculator:
    def add(self, first_input, second_input):
        return first_input + second_input
    def substract(self, first_input, second_input):
        return first_input - second_input
    def multiply(self, first_input, second_input):
        return first_input * second_input
    def divide(self, first_input, second_input):
        return first_input / second_input
    def modulo(self, first_input, second_input):
        return first_input % second_input
    def exponent(self, first_input, second_input):
        return first_input ** second_input
    def square(self, first_input):
        return first_input * first_input
    def percentage(self, first_input):
        return first_input / 100
def replay():
    response = input("Are we done here? (press YES to continue or NO to exit) ")
    if response == "YES":
        calc()
    else:
        print("Thanks for using Simple Python Calculator!")

def calc():
    option = input("""\nSelect the operation to be performed: \n1. addition, 2. subtraction, 3. multiplication, 4. division, 5. modulo, 6. exponent, 7. square, 8. percentage\n""")
    if option == "1" or option == "2" or option == "3" or option == "4" or option == "5" or option == "6":
        print("Enter numbers:")
        input1 = int(input())
        input2 = int(input())
        if option == '1':
            print("The result is: ", Calculator().add(input1, input2))
        elif option == '2':
            print("The result is: ", Calculator().substract(input1, input2))
        elif option == '3':
            print("The result is: ", Calculator().multiply(input1, input2))
        elif option == '4':
            print("The result is: ", Calculator().divide(input1, input2))
        elif option == '5':
            print("The result is: ", Calculator().modulo(input1, input2))
        elif option == '6':
            print("The result is: ", Calculator().exponent(input1, input2))
    elif option == "7" or option == "8":
        print("Enter number:")
        input1 = int(input())
        if option == '7':
            print("The result is: ", Calculator().square(input1))
        elif option == '8':
            print("The result is: ", Calculator().percentage(input1))
    else:
        print("Sorry, There is an error and I can't proceed. Try again!")
        calc()
    replay()

print("Hi, this is Simple Python Calculator")
name = input("What's is your name? ")
print("welcome,", name)
calc()