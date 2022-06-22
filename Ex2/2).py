def fibonacci(limite):
    resultado = [0, 1]
    while resultado[-1] < limite:
        resultado.append(resultado[-2] + resultado[-1])
    return resultado


if __name__ == '__main__':
    num = input('Digite um número:')
    if int(num) in fibonacci(1000):
        print(f'O número informado {num} pertence a sequência fibonacci!')
    else:
        print(f'O número informado {num} não pertence a sequência fibonacci!')
    print(fibonacci(1000))
