#1. Experimente haciendo sumas entre distintos tipos de datos y apunte los resultados.
#   1. Si le salen errores, **no se asuste.** Lea e intente comprender qué significan.
#   Los errores son oportunidades de aprendizaje.
#    Por ejemplo:
#       1. string + string → ?
#       2. string + int → ?
#       3. int + string → ?
#       4. list + list → ?
#       5. string + list → ?
#       6. float + int → ?
#       7. bool + bool → ?

text_one = "First String "
text_two = "Second String"
num_int = 10
num_float = 12.5
my_list = [1,2,3,5,6]
my_second_list = [10,20,30]
my_last_list = ["Costa Rica", "Peru", "Canada"]
flag1 = True
flag2 = True

#1. string + string → ?
result = text_one + text_two
print(result) 

#2. string + int → ?
result = text_one + num_int
print(result) #TypeError: TypeError: can only concatenate str (not "int") to str

#3. int + string → ?
result = num_int + text_two
print(result) #TypeError: unsupported operand type(s) for +: 'int' and 'str'

#4. list + list → ?
result = my_list + my_second_list
print(result)

#4.1 list(string) + list (Int) → ?
result = my_last_list + my_second_list
print(result)

#5. string + list → ?
result = text_one + my_list
print(result) # TypeError: can only concatenate str (not "list") to str

#6. float + int → ?
result = num_float + num_int
print(result)

# 7. bool + bool → ?
result = flag1 + flag2
print(result)
