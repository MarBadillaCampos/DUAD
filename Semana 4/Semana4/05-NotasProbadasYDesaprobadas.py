# 5. Dada `n` cantidad de notas de un estudiante, calcular:
#    1. Cuántas notas tiene aprobadas (mayor o igual a 70).
#    2. Cuántas notas tiene desaprobadas (menor a 70).
#    3. El promedio de todas.
#    4. El promedio de las aprobadas.
#    5. El promedio de las desaprobadas.
counter = 0
pass_score_counter = 0
fail_score_counter = 0
total = 0
pass_result = 0
fail_result = 0

try: 
    max_scores = int(input("Ingrese la cantidad de notas: "))

    for counter in range(1, max_scores + 1):
        current_score = float(input(f"Ingrese la nota número {counter}: "))

        total += current_score

        if current_score >= 70:
            pass_score_counter += 1
            pass_result += current_score
        else:
            fail_score_counter += 1
            fail_result += current_score


    total_average = total / max_scores
    pass_average = pass_result / pass_score_counter if pass_score_counter > 0 else 0
    fail_average = fail_result / fail_score_counter if fail_score_counter > 0 else 0

    print("\n---**** Resultados ***---")
    print(f"Notas aprobadas: {pass_score_counter}")
    print(f"Notas desaprobadas: {fail_score_counter}")
    print(f"Promedio total: {total_average}")
    print(f"Promedio de aprobadas: {pass_average}")
    print(f"Promedio de desaprobadas: {fail_average}")
    
except ValueError:
    print("Ingrese solo números enteros")

