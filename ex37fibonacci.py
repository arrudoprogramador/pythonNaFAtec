numVezes: int = 0
a: int = 0
b: int = 1
i: int = 0

numVezes = int(input("Digite a quantidade desejada de resultados da série:"))

for i in range(numVezes):
    print(a)
    a, b = b, a + b 
    
## Lógica dos corredores.
