print("Bem-vindo à Calculadora em Python!")

 #Recebe Valores
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

 #Recebe Operador
print("Menu de opções")
print("1. Soma")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")
opcao = input("Digite a operação desejada: ")

 #Realiza operação e mostra resultado
if opcao == "1":
    resultado = numero1 + numero2
    print("O resultado é:", resultado)
elif opcao == "2":
    resultado = numero1 - numero2
    print("O resultado é:", resultado)
elif opcao == "3":
    resultado = numero1 * numero2
    print("O resultado é:", resultado)
elif opcao == "4": 
    if numero2 != 0:
        resultado = numero1 / numero2
        print("O resultado é:", resultado)
    else:
        print("Não é possível dividir por zero!")
else:
    print("opcao invalida")