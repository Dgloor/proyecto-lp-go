import ply.lex as lex

# Reserved words
reserved = {
    # Danny Loor
    'break': 'BREAK',
    'case': 'CASE',
    'chan': 'CHAN',
    'const': 'CONST',
    'continue': 'CONTINUE',
    'default': 'DEFAULT',
    'defer': 'DEFER',
    'else': 'ELSE',
    'fallthrough': 'FALLTHROUGH',
    'for': 'FOR',
    'func': 'FUNC',
    'package': 'PACKAGE',
    'range': 'RANGE',
    'return': 'RETURN',
    'select': 'SELECT',
    'struct': 'STRUCT',
    'switch': 'SWITCH',
    'type': 'TYPE',
    'var': 'VAR',
  
    ## Daniel Torres
    'int': 'INTEGER',
    'go': 'GO',
    'goto': 'GOTO',
    'if': 'IF',
    'import': 'IMPORT',
    'interface': 'INTERFACE',
    'map': 'MAP',
    'package': 'PACKAGE',

    ## Diego Arteaga
    'bool': 'BOOL',
    'string': 'STRINGTYPE',
    'else if': 'ELSEIF',
    'else': 'ELSE',
    'var': 'VAR',
    'const': 'CONST',
    'switch': 'SWITCH',
}

# Tokens
tokens = [

    # OPERADORES MATEMATICOS
    'ADICION',
    'RESTA',
    'MULTIPLICACION',
    'DIVISION',
    'MODULO',
    'INCREMENTO',
    'DECREMENTO',

    # OPERADORES DE ASIGNACIÓN
    'ASIGNACION',
    'ASIGNACION_ADICION',
    'ASIGNACION_RESTA',
    'ASIGNACION_MULTI',
    'DECLARACION_ASIGNACION',
    'ASIGNACION_DIVISION',
    'ASIGNACION_MODULO',

    # OPERADORES DE COMPARACIÓN
    'MENOR_IGUAL',
    'IGUAL',
    'DIFERENTE',
    'MAYOR',
    'MENOR',
    'MAYOR_IGUAL',

    #TIPOS DE DATOS

    'INT',
    'DOUBLE',
    'STRING',
    'BOOLEAN',

    # COMPONENTES
    'DOS_PUNTOS',
    'I_LLAVE',
    'D_LLAVE',
    'COMA',
    'I_CORCHETE',
    'D_CORCHETE',
    'IDENTIFICADOR',
    'PUNTO',
    'I_PARENTESIS',
    'D_PARENTESIS',

    # OPERADORES LÓGICOS
    'AND',
    'OR',
    'NOT',

    # IDs
    'ID_VARIABLE',

] + list(reserved.values())

## Daniel Torres

t_ADICION = r'\+'
t_RESTA = r'-'

t_ASIGNACION = r'='
t_ASIGNACION_ADICION = r'\+='

t_MENOR_IGUAL = r'<='
t_IGUAL = r'=='

t_DOS_PUNTOS = r':'
t_I_LLAVE = r'{'
t_D_LLAVE = r'}'
t_COMA = r','

t_AND = r'&&'

## Danny Loor

t_MULTIPLICACION = r'\*'
t_DIVISION = r'/'
t_MODULO = r'%'

t_ASIGNACION_RESTA = r'-='
t_ASIGNACION_MULTI = r'\*='

t_DIFERENTE = r'!='
t_MAYOR = r'>'

t_I_CORCHETE = r'\['
t_D_CORCHETE = r'\]'
t_PUNTO = r'\.'

t_OR = r'\|\|'

## Diego Arteaga

t_INCREMENTO= r"\+\+"
t_DECREMENTO= r"--"

t_DECLARACION_ASIGNACION = r"\:="
t_ASIGNACION_DIVISION= r"\/="
t_ASIGNACION_MODULO= r"%="

t_MENOR= r"<"
t_MAYOR_IGUAL= r">="

t_I_PARENTESIS= r'\('
t_D_PARENTESIS= r'\)'

# Functions Danny Loor
def t_BOOLEAN(t):
    r"(true|false)"
    return t

def t_ID_VARIABLE(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID_VARIABLE')
    return t

def t_STRING(t):
    r'["\'].*["\']'
    t.value = t.value.strip('"').strip("'")
    return t

def t_DOUBLE(t):
    r'\d+\.\d+[e?\d+]*'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

# New Line
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error token
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Ignore tokens
t_ignore_COMMENT = r'\/\/.*'
t_ignore = ' \t'


# Test Diego Arteaga
# data = '''
# //Algoritmo Bubble sort
# func bubbleSort(arr []int, size int) []int {
# 	if size == 1 {
# 		return arr
# 	}

# 	var i = 0
# 	for i < size-1 {
# 		if arr[i] > arr[i+1] {
# 			arr[i], arr[i+1] = arr[i+1], arr[i]
# 		}

# 		i++
# 	}

# 	bubbleSort(arr, size-1)

# 	return arr
# }
# '''



# Build lexer
lexer = lex.lex()
"""
f_dl = open('source.txt')
lexer.input(f_dl.read())

while True:
  tok = lexer.token()
  if not tok:
    break
  print(tok)
  
f_dl.close()
"""  

f = open("test-dt.txt", "r")
lines = f.readlines()
for line in lines:
  lexer.input(line)
  if(len(line.strip()) > 0):
    print('Linea a tokenizar:', line.strip(), ' \n')
  while True:
    tok = lexer.token()
    if not tok:
      break
    print(tok.type, tok.value, tok.lineno, tok.lexpos)
  print('\n')

# Tokenize
while True:
  tok = lexer.token()
  if not tok:
    break  # No more input
  print(tok.type, tok.value, tok.lineno, tok.lexpos)
#print('Mi primer Lexer')

