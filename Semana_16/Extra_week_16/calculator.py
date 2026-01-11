
class Calculator():
 
    def addition(self, number1, number2):
        return  number1 + number2
    
    def multiplication(self, number1, number2):
        return  number1 * number2
    
    def subtraction(self, number1, number2):
        return number1 - number2

    def divide(self, number1, number2):

        if number2 == 0:
            raise ValueError("No se puede dividir por cero")
        
        elif isinstance(number1,str) or isinstance(number2,str):
            raise TypeError('Invalid Input')
        
        return number1 / number2

#num = Calculator()
#print(num.multiplication(-5,-4))



