def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b

print(sumar(3, 5))
print(restar(8, 2))
print(multiplicar(4, 3))
print(dividir(10, 2))