import new_syntax
from datetime import datetime

def log_content(content, filename):
    f =  open(filename, "a")
    f.write("{0} -- {1}: {2}\n".format(datetime.now().strftime("%Y-%m-%d %H:%M"), content[0], content[1]))
    f.close()

while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: continue
    content = [s]
    content.append(new_syntax.valida_regla(s))
    log_content(content, 'logs.txt')