def suma(numero1, numero2):
    return numero1 + numero2

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(500))