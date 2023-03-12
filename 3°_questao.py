import math


a = [ 1, 3, 5, 7]
print('a:', end=' ')
# é o anterior mais em 2
for i in a:
    if i == a[0]:
        print(i, end=', ')
    elif i == a[-1]:
        print(i + 2, end='.')
    else:
        print(i + 2, end=', ')
print()

b = [2, 4, 8, 16, 32, 64]
print('b:', end=' ')
# é o anterior vezes 2
for i in b:
    if i == b[0]:
        print(i, end=', ')
        print(i * 2 , end=', ')
    elif i == b[-1]:
        print(i * 2, end='.')
    else:
        print(i * 2 , end=', ')
print()

c = [0, 1, 4, 9, 16, 25, 36]
# é a sequencia númerica como quadrado perfeito
print('c:', end=' ')

for i in c:
    if i == c[0]:
        print(i, end=', ')
    elif i == c[-1]:
        print(i, end=', ')
        print(int(math.sqrt(i) + 1)**2 , end='.')
    else:
        print(i, end=', ')
print()

d = [4, 16, 36, 64]
# são os números pares da sequencia númerica ao quadrado
print('d:', end=' ')

for i in d:
    if i == d[0]:
        print(i, end=', ')
    elif i == d[-1]:
        print(i, end=', ')
        print(int(math.sqrt(i)+ 2)**2 , end='.')
    else:
        print(i, end=', ')
print()

e = [1, 1, 2, 3, 5, 8, 13]
# é uma sequencia de fibonacci, somando o valor atual com o anterior para dar o proximo
for i in e:
    if i == e[0]:
        print(i, end=', ')
    elif i == e[-1]:
        print(i, end=', ')
        print(i + e[-2] , end='.')
    else:
        print(i, end=', ')
print()

f = [2, 10, 12, 16, 17, 18, 19]
# São valores que começam com d em sua forma escrita por extenso
for i in f:
    if i == f[0]:
        print(i, end=', ')
    elif i == f[-1]:
        print(i, end=', ')
        print(200 , end='.')
    else:
        print(i, end=', ')
print()