def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

numero = int(input("Ingrese un número: "))

primos = []
for i in range(2, numero):
    if es_primo(i):
        primos.append(i)

print("Números primos menores a", numero, ":")
print(primos)
