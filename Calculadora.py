import math


def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ValueError("Não é possível dividir por zero.")
    return a / b


def divisao_inteira(a, b):
    if b == 0:
        raise ValueError("Não é possível dividir por zero.")
    return a // b


def resto(a, b):
    if b == 0:
        raise ValueError("Não é possível dividir por zero.")
    return a % b


def potencia(a, b):
    return a ** b


def raiz_quadrada(a):
    if a < 0:
        raise ValueError("Não existe raiz quadrada real de número negativo.")
    return math.sqrt(a)


def porcentagem(a, b):
    """Calcula b% de a."""
    return a * b / 100


def ler_numero(mensagem):
    """Pede um número ao usuário até que ele digite um valor válido."""
    while True:
        try:
            return float(input(mensagem).replace(",", "."))
        except ValueError:
            print("Valor inválido. Digite um número.")


def mostrar_menu():
    print("\n===== CALCULADORA =====")
    print("1  - Soma (+)")
    print("2  - Subtração (-)")
    print("3  - Multiplicação (*)")
    print("4  - Divisão (/)")
    print("5  - Divisão inteira (//)")
    print("6  - Resto da divisão (%)")
    print("7  - Potência (^)")
    print("8  - Raiz quadrada (√)")
    print("9  - Porcentagem")
    print("0  - Sair")


def main():
    # operações que usam dois números
    operacoes = {
        "1": ("Soma", somar),
        "2": ("Subtração", subtrair),
        "3": ("Multiplicação", multiplicar),
        "4": ("Divisão", dividir),
        "5": ("Divisão inteira", divisao_inteira),
        "6": ("Resto", resto),
        "7": ("Potência", potencia),
        "9": ("Porcentagem", porcentagem),
    }

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "0":
            print("Até logo!")
            break

        try:
            if opcao == "8":
                n = ler_numero("Digite o número: ")
                resultado = raiz_quadrada(n)
                print(f"√{n:g} = {resultado:g}")

            elif opcao in operacoes:
                nome, funcao = operacoes[opcao]
                a = ler_numero("Digite o primeiro número: ")
                b = ler_numero("Digite o segundo número: ")
                resultado = funcao(a, b)
                print(f"{nome}: {resultado:g}")

            else:
                print("Opção inválida. Tente novamente.")

        except ValueError as erro:
            print(f"Erro: {erro}")


if __name__ == "__main__":
    main()