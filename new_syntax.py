from datetime import datetime
import ply.yacc as sintactico
# from main import log_content
from lexico import tokens



def log_content(content, filename):
    f = open(filename, "a")
    f.write("{0} -- {1}\n".format(datetime.now().strftime("%Y-%m-%d %H:%M"), content))
    f.close()

# def p_instrucciones(p):  #puede probar imprimir(var)
#   '''instruccion : asignacion
#                     | impresion '''

def p_go(p):
    '''go : instruccion
            | funcion go
            | funcion'''

def p_body(p):
    '''body : instruccion
            | I_LLAVE instruct_expression D_LLAVE
            | I_LLAVE varias_instrucciones D_LLAVE
            | I_LLAVE varias_instrucciones instruct_expression D_LLAVE
            | I_LLAVE D_LLAVE'''

def p_varias_instrucciones(p):
    '''varias_instrucciones : instruccion
                            | instruccion varias_instrucciones'''

def p_expression_result(p):
    '''instruct_expression : RETURN valor
                            | RETURN resultado'''


def p_instrucciones(p):
    '''instruccion : llamada_func
                     | resultado_inc_dec
                     | expression'''

def p_impresion(p):
    'instruccion : print I_PARENTESIS valores D_PARENTESIS'

def p_declaracion(p):  #puede reconocer a=20
    '''instruccion : VAR ID type ASIGNACION valor
                   | VAR ID ASIGNACION valor
                   | VAR ID ASIGNACION instruccion'''

def p_asignacion(p):
    '''instruccion : ID asignacion valor
          | ID asignacion instruccion'''

def p_funcion(p):
    'funcion : FUNC ID cuerpo_fun'

def p_body_fm(p):
    '''cuerpo_fun : parametrosMetodo body'''

def p_parametros_metodo(p):
    '''parametrosMetodo : I_PARENTESIS parametros D_PARENTESIS type
                        | I_PARENTESIS parametros D_PARENTESIS'''

def p_parametros(p):
    '''parametros : atributo
                  | atributo COMA parametros
                  | '''

def p_llamada_func(p):
    'llamada_func : ID I_PARENTESIS llamada_params D_PARENTESIS'

def p_llamada_params(p):
    '''llamada_params : expression
                      | expression COMA llamada_params'''

#Estructuras de Control

def p_if_condicion(p):
    'instruccion : IF condicion I_LLAVE body D_LLAVE'

def p_else_condicion(p):
    'instruccion : ELSE I_LLAVE body D_LLAVE'

def p_if_else_condicion(p):
    'instruccion : ELSEIF condicion I_LLAVE body D_LLAVE'

def p_for_each(p):
    'instruccion : FOR ID DECLARACION_ASIGNACION RANGE ID I_LLAVE body D_LLAVE'

def p_for_condicion(p):
    'instruccion : FOR instruccion PUNTO_COMA valor PUNTO_COMA ID operador_matematico I_LLAVE body D_LLAVE'

def p_for_map(p):
    'instruccion : FOR ID COMA ID DECLARACION_ASIGNACION RANGE ID I_LLAVE body D_LLAVE'

#Estructuras de Datos

def p_array(p):
    '''instruccion : array_int
    | array_double
    | array_string
    | array_boolean'''
  
def p_array_length(p):
    '''instruccion : array_length_int
    | array_length_double
    | array_length_string
    | array_length_boolean'''

def p_array_con_valores(p):
    '''instruccion : array_con_valores_int
    | array_con_valores_double
    | array_con_valores_string
    | array_con_valores_boolean'''

def p_array_length_con_valores(p):
    '''instruccion : array_length_con_valores_int
    | array_length_con_valores_double
    | array_length_con_valores_string
    | array_length_con_valores_boolean'''

# Arreglo validacion por Daniel Torres
def p_array_int(p):
    'array_int : I_CORCHETE D_CORCHETE INTEGER I_LLAVE D_LLAVE'

def p_array_double(p):
    'array_double : I_CORCHETE D_CORCHETE DOUBLE I_LLAVE D_LLAVE'

def p_array_string(p):
    'array_string : I_CORCHETE D_CORCHETE STRINGTYPE I_LLAVE D_LLAVE'

def p_array_boolean(p):
    'array_boolean : I_CORCHETE D_CORCHETE BOOLEAN I_LLAVE D_LLAVE'

def p_array_length_int(p):
    'array_length_int : I_CORCHETE INT D_CORCHETE INTEGER I_LLAVE D_LLAVE'

def p_array_length_double(p):
    'array_length_double : I_CORCHETE INT D_CORCHETE DOUBLE I_LLAVE D_LLAVE'

def p_array_length_string(p):
    'array_length_string : I_CORCHETE INT D_CORCHETE STRINGTYPE I_LLAVE D_LLAVE'

def p_array_length_boolean(p):
    'array_length_boolean : I_CORCHETE INT D_CORCHETE BOOLEAN I_LLAVE D_LLAVE'

def p_array_con_valores_int(p):
    'array_con_valores_int : I_CORCHETE D_CORCHETE INTEGER I_LLAVE valores_int D_LLAVE'

def p_array_con_valores_double(p):
    'array_con_valores_double : I_CORCHETE D_CORCHETE DOUBLE I_LLAVE valores_double D_LLAVE'

def p_array_con_valores_string(p):
    'array_con_valores_string : I_CORCHETE D_CORCHETE STRINGTYPE I_LLAVE valores_string D_LLAVE'

def p_array_con_valores_boolean(p):
    'array_con_valores_boolean : I_CORCHETE D_CORCHETE BOOLEAN I_LLAVE valores_boolean D_LLAVE'

def p_array_length_con_valores_int(p):
    'array_length_con_valores_int : I_CORCHETE INT D_CORCHETE INTEGER I_LLAVE valores_int D_LLAVE'

def p_array_length_con_valores_double(p):
    'array_length_con_valores_double : I_CORCHETE INT D_CORCHETE DOUBLE I_LLAVE valores_double D_LLAVE'

def p_array_length_con_valores_string(p):
    'array_length_con_valores_string : I_CORCHETE INT D_CORCHETE STRINGTYPE I_LLAVE valores_string D_LLAVE'

def p_array_length_con_valores_boolean(p):
    'array_length_con_valores_boolean : I_CORCHETE INT D_CORCHETE BOOLEAN I_LLAVE valores_boolean D_LLAVE'
# Fin de arreglo
  

def p_map(p):
    'instruccion : MAP I_CORCHETE type D_CORCHETE type I_LLAVE D_LLAVE'

def p_map_make(p):
    'instruccion : MAKE I_PARENTESIS MAP I_CORCHETE type D_CORCHETE type D_PARENTESIS'

def p_map_valores(p):
    'instruccion : MAP I_CORCHETE type D_CORCHETE type I_LLAVE claves_valores D_LLAVE'

def p_struct(p):
    'instruccion : TYPE ID STRUCT I_LLAVE atributos_struct D_LLAVE'

def p_atributos_struct(p):
    '''atributos_struct : atributo
                | atributo atributos_struct'''

def p_atributo(p):
    'atributo : ID type'

def p_declaracion_struct(p):
    'instruccion : init_struct'

def p_init_struct(p):
    '''init_struct : VAR ID ID ASIGNACION ID I_LLAVE valores D_LLAVE
                    | ID DECLARACION_ASIGNACION ID I_LLAVE valores D_LLAVE'''

def p_clave_valor(p):
    '''clave_valor : valor DOS_PUNTOS valor'''

def p_multiple_clave_valor(p):
    '''claves_valores : clave_valor
          | clave_valor COMA claves_valores'''

def p_condicion(p):
    '''condicion : valor
                | I_PARENTESIS valor D_PARENTESIS'''

def p_iteracion_for(p):
    'iteracion_for : ID'

def p_expression_term(p):
    '''expression : valores
                  | resultado
                  | llamada_func
                  | I_PARENTESIS resultado D_PARENTESIS'''

def p_expression_operation(p):
    'resultado : expression operacion_binaria expression'

def p_incremento_decremento(p):
    'resultado_inc_dec : ID operador_matematico'

def p_multiples_valores(p):
    '''valores : valor
          | valor COMA valores'''

def p_multiples_valores_int(p):
    '''valores_int : valor_int
          | valor_int COMA valores_int'''

def p_multiples_valores_double(p):
    '''valores_double : valor_double
          | valor_double COMA valores_double'''

def p_multiples_valores_string(p):
    '''valores_string : valor_string
          | valor_string COMA valores_string'''

def p_multiples_valores_boolean(p):
    '''valores_boolean : valor_boolean
          | valor_boolean COMA valores_boolean'''
  
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
    '''valor : valor_int
          | valor_double
          | valor_string
          | valor_boolean
          | valor_variable'''

def p_valores_int(p):
    '''valor_int : INT'''

def p_valores_double(p):
    '''valor_double : DOUBLE'''

def p_valores_string(p):
    '''valor_string : STRING'''

def p_valores_boolean(p):
    '''valor_boolean : BOOLEAN'''

def p_valores_variable(p):
    '''valor_variable : ID'''

# Error rule for syntax errors
def p_error(p):
    if p:
        error_message = f"Error de sintaxis - Token: {p.type}, Línea: {p.lineno}, Col: {p.lexpos}"
        print(
          error_message
        )
        log_content(error_message, 'logs.txt')
        parser.errok()
    else:
        print("Error de sintaxis Fin de Linea")


# Build the parser
parser = sintactico.yacc()


def valida_regla(s):
    result = parser.parse(s)
    print(result)
