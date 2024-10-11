def sumar(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return "Error: Los operandos deben ser números"
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b

def calcular_potencia(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return "Error: Los operandos deben ser números"
    return a ** b 

# Pruebas de las funciones
print(sumar(3, 5))         # 8
print(restar(8, 2))        # 6
print(multiplicar(4, 3))   # 12
print(dividir(10, 2))      # 5.0
print(restar(10, 2))       # 8
print(calcular_potencia(2, 3))  # 8