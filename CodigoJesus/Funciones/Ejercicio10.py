"""Escribir una función que convierta un número decimal en binario y otra que
convierta un número binario en decimal."""

def decToBin(n):
    num = ""
    val = n
    while val!=1:
        num+=str(val%2)
        val//=2
    num+="1"
    num = ''.join(reversed(num))
    #para obtener la cadena al reves tambien sirve num[::-1]
    return num


def binToDec(n):
    num = 0
    cadena = str(n)
    val = len(cadena)-1
    for i in range(len(cadena)):
        if cadena[i]=="1":
            num+=2**val
        val-=1
    return num



print(decToBin(25))
print(binToDec(10001))
