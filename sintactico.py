import ply.yacc as sintactico
from lexico import tokens

# def p_instrucciones(p):  #puede probar imprimir(var)
#   '''instruccion : asignacion
#                     | impresion '''


def body(p):
  '''body : instruccion'''


def p_impresion(p):
  'instruccion : print I_PARENTESIS arg D_PARENTESIS'


def p_asignacion(p):  #puede reconocer a=20
  'instruccion : VAR type ID ASIGNACION valor'

# def p_def_func(p):
#   'func : FUNC ID I_PARENTESIS argfunc D_PARENTESIS'

# def p_argumento_definicion(p):
#   '''argfunc : type ID'''


def p_argumento(p):
  '''arg : valor
          | valor COMA valor'''


def p_print_options(p):
  '''print : PRINTLN 
          | PRINTF
          | PRINT'''


def p_tipo(p):
  '''type : BOOL
          | STRINGTYPE
          | INTEGER'''

def p_valores(p):
  '''valor : INT
          | DOUBLE
          | STRING
          | ID'''


# Error rule for syntax errors
def p_error(p):
  if p:
    print(
      f"Error de sintaxis - Token: {p.type}, Línea: {p.lineno}, Col: {p.lexpos}"
    )
    parser.errok()
  else:
    print("Error de sintaxis Fin de Linea")


# Build the parser
parser = sintactico.yacc()


def validaRegla(s):
  result = parser.parse(s)
  print(result)
