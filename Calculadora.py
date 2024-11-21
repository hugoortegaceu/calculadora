class Calculadora:
    def sumar(self, x, y):
        return x + y
    def restar(self, x, y):
        return x -y 
    def multiplicar(self, x, y):
        return x * y
    def dividir(self, x, y):
        if y == 0:
            return "Error"
        return x / y 