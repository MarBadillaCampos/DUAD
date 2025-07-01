#1. Cree un pseudocódigo que le pida un `precio de producto` al usuario, calcule su descuento y muestre el precio final tomando en cuenta que:
#    1. Si el precio es menor a 100, el descuento es del 2%.
#    2. Si el precio es mayor o igual a 100, el descuento es del 10%.
#    3. *Ejemplos*:
#        1. 120 → 108
#        2. 40 → 39.2

try: 
    product_price = int(input("Ingrese el precio de un producto: "))
    if product_price < 100:
        final_price = product_price - (product_price * 0.02) 
    else:
        final_price = product_price - (product_price * 0.1) 

    print(f"El precio final de su producto con descuento es: {final_price}")

except TypeError:
    print("Solo números enteros son validos")