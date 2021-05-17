def checa_primo(num):
    contador = 0
    for i in range(1, num + 1):
        if num % i == 0:
            contador += 1
    if contador == 2:
        return True
    else:
        return False


def range_primos(inicio, fim):
    contador = 0
    lista = []
    for fixo in range(inicio, fim + 1):
        contador = 0
        for i in range(1, fim + 1):
            if fixo % i == 0:
                contador += 1
        if contador == 2:
            lista.append(fixo)
    return lista
