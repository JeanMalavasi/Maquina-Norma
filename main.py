from macros import Macros
from entrada import soma, multiplica, fatora

def main():
    print("\n[1] > Somar")
    print("[2] > Multiplicar")
    print("[3] > Fatorar")
    print("[0] > Sair")
    while True:
        escolha = input("\nOque vocẽ quer fazer? ")
        if escolha == '0':
            print("Programa encerrado.")
            exit()
        elif escolha == '1':
            print("\nInsira os valores dos registradores A e B, respectivamente.")
            entrada = int(input("A: "))
            A = Macros(entrada)
            entrada = int(input("B: "))
            B = Macros(entrada)
            C = D = Macros(0)
            instrucaoDeEntrada = soma.get()
            break
        elif escolha == '2':
            print("\nInsira os valores dos registradores A e B, respectivamente.")
            entrada = int(input("A: "))
            A = Macros(entrada)
            entrada = int(input("B: "))
            B = Macros(entrada)
            C = D = Macros(0)
            instrucaoDeEntrada = multiplica.get()
            break
        elif escolha == '3':
            print("\nInsira os valores dos registradores A e B, respectivamente.")
            entrada = int(input("A: "))
            A = Macros(entrada)
            B = C = D = Macros(0)
            instrucaoDeEntrada = fatora.get()
            break
        else:
            print("A opção escolhida não existe.")


    instrucoesDeOperacaoMatriz = montaMatrizDeInstrucao(instrucaoDeEntrada)
    respostaMontada = montaResposta(instrucoesDeOperacaoMatriz, A, B, C, D)
    exibeReposta(respostaMontada)


def exibeReposta(respostaMontada):
    for resp in respostaMontada:
        print(resp)

def montaResposta(instrucaoMatriz, A, B, C, D):
    i = 0
    respostaFinal = []
    resposta = "\nInicio \nA-{}, B-{}, C-{}, D-{}, [{}]".format(A.valor, B.valor, C.valor, D.valor, instrucaoMatriz[i][1])
    respostaFinal.append(resposta)

    while i < len(instrucaoMatriz):
        try:
            if instrucaoMatriz[i][1] == 'ADD':
                if instrucaoMatriz[i][2] == 'A':
                    A.add()
                elif instrucaoMatriz[i][2] == 'B':
                    B.add()
                elif instrucaoMatriz[i][2] == 'C':
                    C.add()
                else:
                    D.add()
                i = instrucaoMatriz[i][3]
                i -= 1
                resposta = ("A-{}, B-{}, C-{}, D-{}, {}, [{}]".format(A.valor, B.valor, C.valor, D.valor, i, instrucaoMatriz[i][1]))
                respostaFinal.append(resposta)

            elif instrucaoMatriz[i][1] == 'SUB':
                if instrucaoMatriz[i][2] == 'A':
                    A.sub()
                elif instrucaoMatriz[i][2] == 'B':
                    B.sub()
                elif instrucaoMatriz[i][2] == 'C':
                    C.sub()
                else:
                    D.sub()
                i = instrucaoMatriz[i][3]
                i -= 1
                resposta = ("A-{}, B-{}, C-{}, D-{}, {}, [{}]".format(A.valor, B.valor, C.valor, D.valor, i + 1, instrucaoMatriz[i][1]))
                respostaFinal.append(resposta)
            
            elif instrucaoMatriz[i][1] == 'ZER':
                if instrucaoMatriz[i][2] == 'A':
                    i = instrucaoMatriz[i][3] if (A.eqZero()) == 1 else instrucaoMatriz[i][4]
                elif instrucaoMatriz[i][2] == 'B':
                    i = instrucaoMatriz[i][3] if (B.eqZero()) == 1 else instrucaoMatriz[i][4]
                elif instrucaoMatriz[i][2] == 'C':
                    i = instrucaoMatriz[i][3] if (C.eqZero()) == 1 else instrucaoMatriz[i][4]
                else:
                    i = instrucaoMatriz[i][3] if (D.eqZero()) == 1 else instrucaoMatriz[i][4]
                i -= 1
                resposta = ("A-{}, B-{}, C-{}, D-{}, {}, [{}]".format(A.valor, B.valor, C.valor, D.valor, i + 1, instrucaoMatriz[i][1]))
                respostaFinal.append(resposta)

        except IndexError:
            return respostaFinal

def montaMatrizDeInstrucao(instrucaoEntrada):
    matrizDeInstrucao = []
    for linha in instrucaoEntrada:
        matrizDeInstrucao += [[linha[0], linha[1], linha[2], linha[3], linha[4]]]
    i = 0
    return matrizDeInstrucao


if __name__ == '__main__':
    main()
    while True:
        option = input("Deseja realizar mais alguma operação? S/s - sim  | N/n - não")
        if option == 'N' or option == 'n':
            print("\nPrograma encerrado.")
            break
        elif option == 'S' or option == 's':
            main()
        else:
            print("Opção invalida.")

