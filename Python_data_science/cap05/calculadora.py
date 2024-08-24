def solicita_numeros():
    """Solicita dois números ao usuário"""
    while True:
        try:
            num1 = float(input("\nDigite o primeiro número: "))
            num2 = float(input("\nDigite o segundo número: "))    
            return num1,num2
        except ValueError:
            print("Entrada Inválida! Somente números")
def mostrar_resultado(operacao,resultado):
    """Função para exibir o resultado de uma operação"""
    print(f"\n{operacao}: {resultado}\n")
def calculadora():
    print("\n******************* Calculadora em Python *******************")
   
    while True:
        opMenuPrincipal = input(
            "1 - Soma\n"
            "2 - Subtração\n"
            "3 - Divisão\n"
            "4 - Multiplicação\n"
            "5 - Sair\n"
            "Escolha uma opção: "
        )
        
        if opMenuPrincipal == "1": # Soma
            num1, num2 = solicita_numeros()
            mostrar_resultado("Soma", num1 + num2)

        elif opMenuPrincipal == "2": # Substração
            num1, num2 = solicita_numeros()
            mostrar_resultado("Subtração", num1 - num2)

        elif opMenuPrincipal == "3":  # Divisão
            num1, num2 = solicita_numeros()
            if num2 != 0: # Validação caso tentem dividir por 0
                mostrar_resultado("Divisão", num1 / num2)
            else:
                print("\nErro! Divisão por zero não é permitida.\n")

        elif opMenuPrincipal == "4":  # Multiplicação
            num1, num2 = solicita_numeros()
            mostrar_resultado("Multiplicação", num1 * num2)

        elif opMenuPrincipal == "5":  # Sair
            print("\nCalculadora encerrada.")
            break

        else:
            print("\nOpção inválida! Por favor, escolha uma opção válida.")

# Executa a calculadora
calculadora()            
                
