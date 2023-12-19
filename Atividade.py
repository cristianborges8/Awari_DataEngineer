#Criar algoritmo que liste toda a sequência de Fibonacci até o número 100;

a, b = 0, 1
print(a)
while b <= 100:
    print(b)
    a, b = b, a + b

# #Criar algoritmo que faça a fatoração do número 1024. (Exemplo de fatoração: 6! = 65432*1)

def fatoracao(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

result_fatoracao = fatoracao(1024)
print(result_fatoracao)

#Criar uma lista de frutas (bananas, maçãs, peras, uvas, laranjas) e fazer um algoritmo para consultar se uma fruta existe na lista.
#Caso não exista, adicionar a nova fruta. O programa só deve encerrar a brincadeira quando o usuário informar o número 999.

frutas = ["banana", "maçã", "pera", "uva", "laranja"]

while True:
    fruta = input("Digite o nome de uma fruta (ou 999 para sair): ")

    if fruta == "999":
        break

    if fruta in frutas:
        print(f"A fruta {fruta} já existe na lista.")
    else:
        frutas.append(fruta)   
        print(f"A fruta {fruta} foi adicionada à lista.")

print("Lista final de frutas:", frutas)

    

