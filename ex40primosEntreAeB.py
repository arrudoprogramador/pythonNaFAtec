num: int = 0

a = int(input("Número inicial: "))
b = int(input("Número final: "))

print(f"Números primos entre {a} e {b}: ")

for num in range(a, b + 1):
    divisores = 0

    for i in range(1, num + 1):
        if num % i == 0:
            divisores += 1
    if divisores == 2:
        print(num)

