num = [0] * 10

for i in range(10):
    num[i] = int(input(f"Digite o {i+1} número:"))

    numMaior = num[0]
    numMenor = num[0]

for i in range(10):
    if(num[i] > numMaior):
        numMaior = num[i]
    if(num[i] < numMenor):
        numMenor = num[i]

print("Maior número:", numMaior, "\n"
        "Número menor:", numMenor)