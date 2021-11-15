linha1 = input().split(' ')
linha2 = input().split(' ')

quant1 = int(linha1[1])
preco1 = float(linha1[2])

quant2 = int(linha2[1])
preco2 = float(linha2[2])

print(f'VALOR A PAGAR: R$ {((quant1 * preco1) + (quant2 * preco2)):.2f}')
