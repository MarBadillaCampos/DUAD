#Cree un programa que le pida tres números al usuario y muestre el mayor.

try:
    first_num = int(input("Ingrese el valor del primero numero: "))
    second_num = int(input("Ingrese el valor del segundo numero: "))
    third_num = int(input("Ingrese el valor del Tercer numero: "))

    if first_num > second_num:
        max_num = first_num
    elif second_num > third_num:
        max_num = second_num
    else:
        max_num = third_num   
    print(f"Mayor: {max_num}")

except ValueError:
    print("Ingrese solo números enteros")