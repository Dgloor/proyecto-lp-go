import sintactico

while True:
  try:
    s = input('calc > ')
  except EOFError:
    break
  if not s: continue
  sintactico.validaRegla(s)
'''Ejemplos que por ahora puede validar
int a=20
var variable float32 =30.2
imprimir(var)
imprimir(20.3)
'''
'''
Para practicar implemente las siguientes reglas:
a=30+23
var=20-310*292/23
cond=20>variable
if var>10: imprimir(True)
'''