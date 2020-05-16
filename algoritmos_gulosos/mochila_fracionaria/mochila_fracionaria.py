itens, capacidade = map(int, input().split())

pesos = []
for i in range(itens):
    c, w = map(int, input().split())
    pesos.append((c, w, c * 1.0 / w))

ordenadoPeso = sorted(pesos, key=lambda x: x[2], reverse=True)
total = 0
for X in ordenadoPeso:
    if capacidade >= X[1]:
        capacidade -= X[1]
        total += X[0]
    else:
        total += capacidade * 1.0 / X[1] * X[0]
        break

print(format(total, '.3f'))