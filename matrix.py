numero = [[1,2,3], [4,5,6], [7,8,9]]

for i in range(len(numero)):
    for p in range(len(numero)):
        if numero[i][p] % 2 == 0:
            print(f"Numero par {numero[i][p]}")