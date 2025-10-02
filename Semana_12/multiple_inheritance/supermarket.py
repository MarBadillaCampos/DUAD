class Fruit:


    def __init__(self, name, quantity):
        self.fruit_name = name
        self.fruit_quantity = int(quantity)

    def fruit_price(self):
        return self.fruit_quantity * 500


class Meat:

    def __init__(self, name, quantity):
        self.meat_name = name
        self.meat_quantity = int(quantity)

    def meat_price(self):
        return self.meat_quantity * 2500


class Vegetable:

    def __init__(self, name, quantity):
        self.veg_name = name
        self.veg_quantity = int(quantity)

    def veg_price(self):
        return self.veg_quantity * 250


class Supermarket(Fruit, Meat, Vegetable):
    def __init__(self, fruit_name, fruit_cant, meat_name, meat_cant, veg_name, veg_cant):
        Fruit.__init__(self, fruit_name, fruit_cant)
        Meat.__init__(self, meat_name, meat_cant)
        Vegetable.__init__(self, veg_name, veg_cant)

    def total_price(self):
        return self.fruit_price() + self.meat_price() + self.veg_price()


def main():
    supermarket = Supermarket(
        fruit_name="Manzana", fruit_cant=5,
        meat_name="Pork Meat", meat_cant=2,
        veg_name="Potato", veg_cant=15
    )

    print(f"Fruta: {supermarket.fruit_name} - Total: {supermarket.fruit_price()}")
    print(f"Carne: {supermarket.meat_name} - Total: {supermarket.meat_price()}")
    print(f"Vegetal: {supermarket.veg_name} - Total: {supermarket.veg_price()}")
    print(f"TOTAL: {supermarket.total_price()}")


if __name__ == "__main__":
    main()
