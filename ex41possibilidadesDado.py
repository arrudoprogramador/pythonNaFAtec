resultado = 0

for i in range(7):
    for num in range(7):
        soma = num + i
        if soma == 7:
            resultado += 1
            print(f"Possibilidade {resultado}°:", num," + ", i)

print("Existem ", resultado, "possibilidades da soma ser 7")