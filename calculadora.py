print("Bem-vindo à Calculadora em Python!")
 
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

print("Menu de opções")
print("1. Soma")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")
opcao = input("Digite a operação desejada: ")

if opcao == "1":
    resultado = numero1 + numero2
elif opcao == "2":
    resultado = numero1 - numero2
elif opcao == "3":
    resultado = numero1 * numero2
elif opcao == "4": 
    if numero2 != 0:
        resultado = numero1 / numero2
    else:
        print("Não é possível dividir por zero!")
else:
    print("opcao invalida")
