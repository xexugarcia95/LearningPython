"""Escribir una función que reciba un número entero positivo y devuelva
su factorial."""

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

print(str(factorial(5)))
