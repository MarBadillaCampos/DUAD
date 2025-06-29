#2. Cree un algoritmo que le pida al usuario una velocidad en km/h y la convierta a m/s. 
# Recuerda que `1 km == 1000m` y `1 hora == 60 minutos * 60 segundos`.
#    1. *Ejemplos*:
#        1. 73 → 20.27
#        2. 50 → 13.88
#        3. 120 → 33.33
try:
    user_speed = int(input("Ingrese una velocidad en km/h: "))
    final_speed = (user_speed * 1000) / 3600
    print(f"Su velocidad en m/s es de: {final_speed}")
except ValueError:
    print("Error: Por favor, ingrese solo números enteros.")