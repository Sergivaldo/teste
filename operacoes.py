def somar(a: float, b: float) -> float:
    return a + b


def subtrair(a: float, b: float) -> float:
    return a - b


def multiplicar(a: float, b: float) -> float:
    return a * b


def dividir(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Divisão por zero não é permitida.")
    return a / b


if __name__ == "__main__":
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))

    print(f"\nResultados:")
    print(f"  Soma:        {somar(a, b)}")
    print(f"  Subtração:   {subtrair(a, b)}")
    print(f"  Multiplicação: {multiplicar(a, b)}")

    try:
        print(f"  Divisão:     {dividir(a, b)}")
    except ValueError as e:
        print(f"  Divisão:     Erro — {e}")
