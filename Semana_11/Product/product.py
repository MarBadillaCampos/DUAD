class Product:
    def __init__(self, name, price, cant):
        self.name = name
        self.price = price
        self.cant = cant

    def __str__(self):
        return f"{self.name} - Price: {self.price}, Cant: {self.cant}"


class Inventory:
    def __init__(self):
        self.inventory = []

    def add_product(self, product):
        self.inventory.append(product)

    def show_products(self):
        print("\nProducts:")
        for i in self.inventory:
            print(i)

    def total_value(self):
        total = 0
        for p in self.inventory:
            total += p.price * p.cant
        return total



product1 = Product("Milk", 200, 1)
product2 = Product("Cookies", 400, 5)
product3 = Product("Rice", 1200, 1)

inv = Inventory()


inv.add_product(product1)
inv.add_product(product2)
inv.add_product(product3)


inv.show_products()


print("\nTotal:", inv.total_value())
