#Cree un programa que itere e imprima los valores de dos listas del mismo tamaño al mismo tiempo.
#1. Ejemplos:
#2. `first_list = [’Hay’, 'en’, 'que’, 'iteración’, 'indices’, 'muy’]`
#`second_list = [’casos’, 'los’, 'la’, 'por’, 'es’, 'util’]` ->
#Hay casos
#en los
#que la
#iteración por
#indice es
#muy util
first_list = ['Hay', 'en', 'que', 'iteración', 'indices', 'muy']
second_list = ['casos', 'los', 'la', 'por', 'es','util']

for index in range(0,len(first_list)):
    record = first_list[index]
    record2= second_list[index]
    print(f'{record} {record2}')




