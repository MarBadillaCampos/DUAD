def menu():
    print("\n[+] Add")
    print("[-] Subtract")
    print("[*] Multiply")
    print("[%] Divide")
    print("[C] Clear Result")
    print("[x] Exit\n")

def get_input():
    return input("Input: ").strip().lower()

def add(result, num):
    return result + num

def subtract(result, num):
    return result - num

def multiply(result, num):
    return result * num

def divide(result, num):
    string = "Error: division by zero."
    try:
        return result / num
    
    except ZeroDivisionError:
        return string

def calculator():
    result = 0
    function = None
    operations = ['+', '-', '*', '%']

    print(f"{result}")

    while True:
        option = get_input()

        if option == 'x':
            break

        elif option == 'c':
            result = 0
            function = None
            print(f"{result}")
            continue

        elif option in operations:
            function = option

        else:
            try:
                num = float(option)
                if function is None:
                    result = num
                else:
                    temp = None
                    if function == '+':
                        temp = add(result, num)
                    elif function == '-':
                        temp = subtract(result, num)
                    elif function == '*':
                        temp = multiply(result, num)
                    elif function == '%':
                        temp = divide(result, num)

                    if temp is not None:
                        result = temp

                    function = None
                print(f"{result}")
            except ValueError:
                print("Invalid input")

def main():
    menu()
    calculator()

if __name__ == '__main__':
    main()
