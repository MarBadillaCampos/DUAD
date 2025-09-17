class Animal:
    def __init__(self,name):
        self.name = name
    
    def speak(self):
        return 'Hace un sonido'


class Dog(Animal):
    def __init__(self,name):
        super().__init__(name)
    
    def speak(self):
        return 'Guau'

class Cat(Animal):
    def __init__(self,name):
        super().__init__(name)
    
    def speak(self):
        return 'Miau'
        
dog = Dog('Caramelo')
cat = Cat('Manchas')
print(dog.speak())
print(cat.speak())