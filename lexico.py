import ply.lex as lex

# Reserved words
reserved = {
  # Danny Loor
  'break': 'BREAK',
  'case': 'CASE',
  'chan': 'CHAN',
  'continue': 'CONTINUE',
  'default': 'DEFAULT',
  'defer': 'DEFER',
  'fallthrough': 'FALLTHROUGH',
  'for': 'FOR',
  'func': 'FUNC',
  'range': 'RANGE',
  'return': 'RETURN',
  'select': 'SELECT',
  'struct': 'STRUCT',
  'type': 'TYPE',
  'make': 'MAKE',

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
  'else': 'ELSE',
  'var': 'VAR',
  'const': 'CONST',
  'switch': 'SWITCH',
  'float32': 'FLOAT32',
  'float64': 'FLOAT64',
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

  # TIPOS DE DATOS
  'INT',
  'DOUBLE',
  'STRING',
  'BOOLEAN',

  # COMPONENTES
  'DOS_PUNTOS',
  'PUNTO_COMA',
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

  'PRINTLN',
  'PRINTF',
  'PRINT',

  # IDs
  'ID',

  # Auxiliar
  'ELSEIF',
] + list(reserved.values())

## Daniel Torres
t_ADICION = r'\+'
t_RESTA = r'-'

t_ASIGNACION = r'='
t_ASIGNACION_ADICION = r'\+='

t_MENOR_IGUAL = r'<='
t_IGUAL = r'=='

t_DOS_PUNTOS = r':'
t_PUNTO_COMA = r';'
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
t_INCREMENTO = r"\+\+"
t_DECREMENTO = r"--"

t_DECLARACION_ASIGNACION = r"\:="
t_ASIGNACION_DIVISION = r"\/="
t_ASIGNACION_MODULO = r"%="

t_MENOR = r"<"
t_MAYOR_IGUAL = r">="

t_I_PARENTESIS = r'\('
t_D_PARENTESIS = r'\)'

# Funciones

# def t_FMTFUNC(t):
#   r'fmt\.'

def t_PRINTLN(t):
    r'fmt\.Println'
    return t


def t_PRINTF(t):
    r'fmt\.Printf'
    return t

def t_PRINT(t):
    r'fmt\.Print'
    return t


def t_ELSEIF(t):
    r'else\sif'
    return t


def t_BOOLEAN(t):
    r'(true|false)'
    return t


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
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

# Build lexer
lexer = lex.lex()

# print("=== Test Daniel Torres ===")
# f_dt = open('test-dt.txt')
# lexer.input(f_dt.read())

# f_dt.seek(0, 0)
# for line in f_dt.readlines():
#   print(line.strip('\n'))
# print()

# while True:
#   tok = lexer.token()
#   if not tok:
#     break
#   print(tok)

# f_dt.close()

# print("\n\n=== Test Danny Loor ===")
# f_dl = open('test-dl.txt')
# lexer.input(f_dl.read())

# f_dl.seek(0, 0)
# for line in f_dl.readlines():
#   print(line.strip('\n'))
# print()

# while True:
#   tok = lexer.token()
#   if not tok:
#     break
#   print(tok)

# f_dl.close()

# print("\n\n=== Test Diego Arteaga ===")
# f_da = open('test-da.txt')
# lexer.input(f_da.read())

# f_da.seek(0, 0)
# for line in f_da.readlines():
#   print(line.strip('\n'))
# print()

# while True:
#   tok = lexer.token()
#   if not tok:
#     break
#   print(tok)

# f_da.close()