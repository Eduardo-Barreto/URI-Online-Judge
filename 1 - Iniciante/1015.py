from math import sqrt

entrada1 = input().split(' ')
x1, y1 = [float(i) for i in entrada1]

entrada2 = input().split(' ')
x2, y2 = [float(i) for i in entrada2]

print(f'{(sqrt((x2-x1)**2 + (y2-y1)**2)):.4f}')
