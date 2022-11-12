import ply.lex as lex

# Reserved words
reserved = {
    # Inicio: Danny Loor
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
    'go': 'GO',
    'goto': 'GOTO',
    'if': 'IF',
    'import': 'IMPORT',
    'interface': 'INTERFACE',
    'map': 'MAP',
    'package': 'PACKAGE',
    'range': 'RANGE',
    'return': 'RETURN',
    'select': 'SELECT',
    'struct': 'STRUCT',
    'switch': 'SWITCH',
    'type': 'TYPE',
    'var': 'VAR',
    # Fin: Danny Loor

    ## Diego Arteaga
    'bool': 'BOOL',
    'string': 'STRING',
    'else if': 'ELSEIF',
    'else': 'ELSE',

    ## Diego Arteaga
    'var': 'VAR',
    'const': 'CONST',
    'switch': 'SWITCH',

}

# Tokens
tokens = [

    # OPERADORES MATEMATICOS
    ## Daniel Torres
    'ADICION',
    'RESTA',
    ##Danny Loor
    'MULTIPLICACION',
    'DIVISION',
    'MODULO',

    ## Diego Arteaga
    'INCREMENTO',
    'DECREMENTO',

    # OPERADORES DE ASIGNACIÓN
    ## Daniel Torres
    'ASIGNACION',
    'ASIGNACION_ADICION',

    ##Danny Loor
    'ASIGNACION_RESTA',
    'ASIGNACION_MULTI',

    ## Diego Arteaga
    'DECLARACION_ASIGNACION'
    'ASIGNACION_DIVISION',
    'ASIGNACION_MODULO',

    # OPERADORES DE COMPARACIÓN
    ## Daniel Torres
    'MENOR_IGUAL',
    'IGUAL',

    ##Danny Loor
    'DIFERENTE',
    'MAYOR',

    ## Diego Arteaga
    'MENOR',
    'MAYOR_IGUAL',

    #TIPOS DE DATOS

    ##Danny Loor
    'INT',
    'DOUBLE',
    'STRING',

    ## Diego Arteaga
    'BOOLEAN',

    # COMPONENTES
    ## Daniel Torres
    'DOS_PUNTOS',
    'I_LLAVE',
    'D_LLAVE',
    'COMA',

    ##Danny Loor
    'I_CORCHETE',
    'D_CORCHETE',
    'VARIABLE',
    'PUNTO',

    ## Diego Arteaga
    'I_PARENTESIS',
    'D_PARENTESIS',

    # OPERADORES LÓGICOS
    ## Daniel Torres
    'AND',
    ##Danny Loor
    'OR',

    ## Diego Arteaga
    'NOT',

] + list(reserved.values())

# Regexs
t_ASSIGN = r'='
t_sum = r'\+'

## Diego Arteaga

t_INCREMENTO= r"\+\+"
t_DECREMENTO= r"--"

t_DECLARACION_ASIGNACION = r":="
t_ASIGNACION_DIVISION= r"/="
t_ASIGNACION_MODULO= r"%="

t_MENOR= r"<"
t_MAYOR_IGUAL= r">="

t_CADENA= r'"[^"]*"'

t_I_PARENTESIS= r'\('
t_D_PARENTESIS= r'\)'

# Functions Danny Loor
def t_BOOLEAN(t):
    r"(true|false)"
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'VARIABLE')
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
# \\\\ Algoritmo Bubble sort
# /*
#  * Ordenamiento de menor a mayor
#  * Recibe un arreglo y el número de elementos que contiene el mismo
#  */
# func BubbleSort(array []int) []int {
# 	for i := 0; i < len(array)-1; i++ {
# 		for j := 0; j < len(array)-i-1; j++ {
# 			if array[j] > array[j+1] {
# 				array[j], array[j+1] = array[j+1], array[j]
# 			}
# 		}
# 	}
# 	return array
# }
# '''



# Build lexer
lexer = lex.lex()

"""
lexer.input(f.read())

while True:
  tok = lexer.token()
  if not tok:
    break
  print(tok)
  
"""
