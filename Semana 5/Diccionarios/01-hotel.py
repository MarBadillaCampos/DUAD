#1. Cree un diccionario que guarde la siguiente información sobre un hotel:
#   - `nombre`
#   - `numero_de_estrellas`
#    - `habitaciones`
#- El value del key de `habitaciones` debe ser una lista, y cada habitación debe tener la siguiente información:
#    - `numero`
#    - `piso`
#   - `precio_por_noche`

hotel_ta = {
    'nombre': 'Té de Árbol',
    'numero_de_estrellas': '5',
    'habitaciones': [
        {"numero": 11, "piso": 1, "precio_por_noche": 100},
        {"numero": 10, "piso": 2, "precio_por_noche": 300},
        {"numero": 15, "piso": 3, "precio_por_noche": 500},
        {"numero": 20, "piso": 4, "precio_por_noche": 800}
    ]
}

for key, value in hotel_ta.items():
    if key == 'habitaciones':
        print(f'{key}:')
        for room in value:
            print(f"Número: {room['numero']}, Piso: {room['piso']}, Precio por noche: ${room['precio_por_noche']}")
    else:
        print(f'{key}: {value}')
    


