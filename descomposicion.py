def descomposicion_prima(numero):
    factores_primos = []
    divisor = 2

    while divisor <= numero:
        if numero % divisor == 0:
            factores_primos.append(divisor)
            numero = numero / divisor
        else:
            divisor += 1

    return factores_primos

numero = int(input("Ingrese un número: "))

resultado = descomposicion_prima(numero)

print("Descomposición prima de", numero, ":")
print(resultado)
