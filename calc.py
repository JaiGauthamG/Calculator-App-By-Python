import math

def show_ops():
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square")
    print("6. Cube")
    print("7. Power")
    print("8. Modulus")
    print("9. Square Root")

def get_op_from_user():
    op_user = int(input("Select an operator: "))
    return op_user

def ask_user_numbers():
    num1 = int(input("Enter the First Number: "))
    num2 = int(input("Enter the Second Number: "))
    
    return num1, num2

def calc_user_numbers(num1, num2):
    addition =  + num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    division = num1 / num2 if num2 != 0 else print("The Division can't be made by 0")
    power = num1 ** num2
    modulus = num1 % num2
    
    return addition, subtraction, multiplication, division, power, modulus

def main():
    show_ops()
    op = get_op_from_user()
    
    if op == 5:
        num1 = int(input("Enter The Number: "))
        sqr = num1 ** 2
        print(f"The Square of {num1} is {sqr}")
    elif op == 6:
        num1 = int(input("Enter The Number: "))
        cube = num1 ** 3
        print(f"The Cube of {num1} is {cube}")
    elif op == 9:
        num1 = int(input("Enter the Number: "))
        sqrt = math.sqrt(num1)
        print(f"The Square Root of {num1} is {sqrt}")
    elif op == 7:
        num1 = int(input("Enter the Base: "))
        num2 = int(input(f"Base {num1} raised to ?: "))
        pwr = num1 ** num2
        print(f"The Base {num1} raised to {num2} is {pwr}")
    else:
        num1, num2 = ask_user_numbers()
        result = calc_user_numbers(num1, num2)
        
        if op == 1:
            print(f"The Addition of {num1} and {num2} is {result[0]}")
        elif op == 2:
            print(f"The Subtraction of {num1} and {num2} is {result[1]}")
        elif op == 3:
            print(f"The Multiplication of {num1} and {num2} is {result[2]}")
        elif op == 4:
            print(f"The Division of {num1} and {num2} is {result[3]}")
        elif op == 8:
            print(f"The Modulus of {num1} and {num2} is {result[5]}")
        else:
            print("Invalid Option! Select a number between 1 - 9!")
            
main()