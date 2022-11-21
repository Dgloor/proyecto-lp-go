import ply.yacc as sintactico
from lexico import tokens

# def p_instrucciones(p):  #puede probar imprimir(var)
#   '''instruccion : asignacion
#                     | impresion '''

def body(p):
  '''body : instruccion'''

def p_impresion(p):
  'instruccion : print I_PARENTESIS valores D_PARENTESIS'

def p_declaracion(p):  #puede reconocer a=20
  'instruccion : VAR ID type ASIGNACION valor'

def p_asignacion(p):
  'instruccion : ID asignacion valor'

def p_incremento_decremento(p):
  'instruccion : ID operador_matematico'

def p_array(p):
  'instruccion : I_CORCHETE D_CORCHETE type I_LLAVE D_LLAVE'
  
def p_array_length(p):
  'instruccion : I_CORCHETE INT D_CORCHETE type I_LLAVE D_LLAVE'

def p_array_con_valores(p):
  'instruccion : I_CORCHETE D_CORCHETE type I_LLAVE valores D_LLAVE'

def p_array_length_con_valores(p):
  'instruccion : I_CORCHETE INT D_CORCHETE type I_LLAVE valores D_LLAVE'

# def p_def_func(p):
#   'func : FUNC ID I_PARENTESIS argfunc D_PARENTESIS'

# def p_argumento_definicion(p):
#   '''argfunc : type ID'''

def p_multiples_valores(p):
  '''valores : valor 
          | valor COMA valores'''
  
def p_operacion_mat(p):
  'valor : valor operacion_binaria valor'

def p_print_options(p):
  '''print : PRINTLN 
          | PRINTF
          | PRINT'''

def p_tipo(p):
  '''type : BOOL
          | STRINGTYPE
          | INTEGER
          | FLOAT32
          | FLOAT64'''

def p_operacion_mat_var(p):
  '''operador_matematico : INCREMENTO
          | DECREMENTO'''

def p_operadores_asignacion(p):
  '''asignacion : ASIGNACION
          | ASIGNACION_ADICION
          | ASIGNACION_RESTA
          | ASIGNACION_MULTI
          | DECLARACION_ASIGNACION
          | ASIGNACION_DIVISION
          | ASIGNACION_MODULO'''

def p_operacion_mat_simbolos(p):
  '''operacion_binaria : ADICION
          | RESTA
          | MULTIPLICACION
          | DIVISION
          | MODULO'''

def p_operacion_comp_simbolos(p):
  '''operacion_binaria : MENOR_IGUAL
          | IGUAL
          | DIFERENTE
          | MAYOR
          | MAYOR_IGUAL
          | MENOR'''

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
