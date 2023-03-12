def fibonacci(valor):
    resultado = [0, 1]
    while resultado[-1] < valor:
        resultado.append(resultado[-1]+resultado[-2])
    if valor in resultado:
        print(f'O valor {valor}, pertence ao Fibonacci.')
    else:
        print(f'O valor {valor}, não pertence ao Fibonacci.')
    return resultado

n = fibonacci(int(input('Informe um número que gostaria de verificar se pertence ao fibonacci: ')))

for fib in n:
    if fib == n[-1]:
        print(fib, end='.')
    else:
        print(fib, end=', ')
