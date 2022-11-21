import sintactico
from datetime import datetime

def log_content(content, filename):
    f = open(filename, "a")
    f.write("{0} -- {1}: {2}\n".format(datetime.now().strftime("%Y-%m-%d %H:%M"), content[0], content[1]))
    f.close()

while True:
  try:
    s = input('calc > ')
  except EOFError:
    break
  if not s: continue
  content = [s]
  content.append(sintactico.validaRegla(s))
  log_content(content, 'logs.txt')
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