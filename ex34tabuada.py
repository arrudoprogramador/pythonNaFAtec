## Declaração de variáveis
num: int = 0
resultado: int = 0

## Início
num = int(input("Digite o número da tabuada desejado:"))
print(f"Tabuada do {num}")

for i in range(0, 11):
    resultado = i * num
    print(f"{num} X {i} =", resultado)

## Fim
