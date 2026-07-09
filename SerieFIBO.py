def fibonacci_iterativo(n):
    if n < 0:
        return "Introduce un número válido"
    
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

print(fibonacci_iterativo(7))  # Salida: 13
