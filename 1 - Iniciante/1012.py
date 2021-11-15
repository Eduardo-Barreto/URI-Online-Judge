entrada = input().split(' ')
a, b, c = [float(i) for i in entrada]

TRIANGULO = a*c/2
CIRCULO = 3.14159*(c**2)
TRAPEZIO = ((a+b)/2)*c
QUADRADO = b**2
RETANGULO = a*b

result = {
  'TRIANGULO': TRIANGULO,
  'CIRCULO': CIRCULO,
  'TRAPEZIO': TRAPEZIO,
  'QUADRADO': QUADRADO,
  'RETANGULO': RETANGULO
}

for c, v in result.items():
  print(f'{c}: {v:.3f}')
