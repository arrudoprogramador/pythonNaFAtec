graos: int = 1
casa: int = 1
total: int = 0

for i in range(64):
    print(f"Casa: {casa} Quantidade: {graos}")
    casa += 1
    graos = graos + graos
    total += graos

print("Total de grãos: ", (total-1))