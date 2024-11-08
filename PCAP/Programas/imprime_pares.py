def imprime_pares(lista):
    for num in lista:
        if int(num) % 2 == 0:
            print(num, end=' ')
        else:
            continue