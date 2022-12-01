from datetime import datetime
import ply.yacc as sintactico
# from main import log_content
from lexico import tokens, AnalyzerException

variables = {}
booleanos = ("true", "false")

precedence = (
    ('left', 'ADICION', 'RESTA'),
    ('left', 'MULTIPLICACION', 'DIVISION'),
)

def oparation_number(operador, p_valor, s_valor):
    if operador == '+':
        return p_valor + s_valor
    if operador == '-':
        return p_valor - s_valor
    elif operador == '*':
        return p_valor * s_valor
    elif operador == '/':
        return p_valor / s_valor
    elif operador == '%':
        return p_valor % s_valor

def operation(operador, p_valor, s_valor):
    p_valor = str(p_valor)
    s_valor = str(s_valor)
    if p_valor.find(".") == -1 and s_valor.find(".") == -1:
        if (p_valor.isdigit() and s_valor.isdigit()):
            p_valor = int(p_valor)
            s_valor = int(s_valor)
            return oparation_number(operador, p_valor, s_valor)
    else:
        return oparation_number(operador, float(p_valor), float(s_valor))

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
            | funcion
            | instruccion go'''

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
    '''instruct_expression : RETURN valor_string
                            | RETURN expression
                            | RETURN expression_bool'''


def p_instrucciones(p):
    '''instruccion : llamada_func
                     | resultado_inc_dec
                     | expression'''

def p_impresion(p):
    'instruccion : print I_PARENTESIS valores D_PARENTESIS'

def p_declaracion(p):  # puede reconocer a=20
    '''instruccion : declaracion_comun
                   | declara_int
                   | declara_double
                   | declara_string
                   | declara_bool
                   | decla_header ASIGNACION instruccion
                   | decla_header array_type_spec ASIGNACION instruccion
                   | empty_struct
                   | empty_array'''

def p_asignacion(p):
    '''instruccion : ID asignacion valor
          | ID asignacion instruccion'''




def p_declaraciones_comunes(p):
    '''declaracion_comun : decla_header ASIGNACION valor'''

def p_declaracion_int(p):
    'declara_int : decla_header INTEGER ASIGNACION valor_int'

def p_declaracion_double(p):
    'declara_double : decla_header floating_type ASIGNACION valor_double'

def p_declaracion_string(p):
    'declara_string : decla_header STRINGTYPE ASIGNACION valor_string'

def p_declaracion_boolean(p):
    'declara_bool : decla_header BOOL ASIGNACION valor_boolean'

def p_declara_empty_struct_var(p): #Diego Arteaga - Structs
    'empty_struct : decla_header ID'

def p_declara_empty_array(p):
    'empty_array : decla_header array_type_spec'

def p_declara_header(p):
    '''decla_header : VAR ID'''

def p_funcion(p):
    '''funcion : FUNC ID cuerpo_fun
               | funcion_no_type'''

def p_funct_notype(p):
    'funcion_no_type : FUNC ID parametros_sin_tipo body'

def p_body_fm(p):
    '''cuerpo_fun : parametrosMetodo body'''

def p_parametros_metodo(p):
    '''parametrosMetodo : parametrosMetodoInt
                        | parametrosMetodoString
                        | parametrosMetodoDouble
                        | parametrosMetodoBool
                        | parametros_sin_tipo'''

def p_parametros_metodo_int(p):
    'parametrosMetodoInt : parametros_sin_tipo INTEGER'

def p_parametros_metodo_string(p):
    'parametrosMetodoString : parametros_sin_tipo STRINGTYPE'

def p_parametros_metodo_double(p):
    'parametrosMetodoDouble : parametros_sin_tipo floating_type'

def p_parametro_metodo_bool(p):
    'parametrosMetodoBool : ID BOOL'

def p_parametros_metodo_notype(p):
    '''parametros_sin_tipo : I_PARENTESIS parametros D_PARENTESIS'''

def p_parametros(p):
    '''parametros : atributo
                  | atributo COMA parametros
                  | valores type'''

def p_llamada_func(p):
    'llamada_func : ID I_PARENTESIS llamada_params D_PARENTESIS'

def p_llamada_params(p):
    '''llamada_params : expression
                      | expression COMA llamada_params
                      | expression_bool
                      | expression_bool COMA llamada_params
                      | valores_string'''

#Estructuras de Control

def p_control_structs(p):
    '''instruccion : if_struct
    | if_else_struct'''

#if - Diego Arteaga
def p_if_condicion(p):
    'if_struct : IF condicion body'


def p_else_condicion(p):
    '''if_else_struct : if_struct ELSE body
                      | many_elseif ELSE body
                      | many_elseif'''

def p_many_elseif(p):
    '''many_elseif : else_if
                   | else_if many_elseif'''

def p_if_else_condicion(p):
    'else_if : ELSE IF condicion body'


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
    'array_double : I_CORCHETE D_CORCHETE floating_type I_LLAVE D_LLAVE'

def p_array_string(p):
    'array_string : I_CORCHETE D_CORCHETE STRINGTYPE I_LLAVE D_LLAVE'

def p_array_boolean(p):
    'array_boolean : I_CORCHETE D_CORCHETE BOOLEAN I_LLAVE D_LLAVE'

def p_array_length_int(p):
    'array_length_int : array_length INTEGER I_LLAVE D_LLAVE'

def p_array_length_double(p):
    'array_length_double : array_length floating_type I_LLAVE D_LLAVE'

def p_array_length_string(p):
    'array_length_string : array_length STRINGTYPE I_LLAVE D_LLAVE'

def p_array_length_boolean(p):
    'array_length_boolean : array_length BOOLEAN I_LLAVE D_LLAVE'

def p_array_con_valores_int(p):
    'array_con_valores_int : I_CORCHETE D_CORCHETE INTEGER I_LLAVE valores_int D_LLAVE'

def p_array_con_valores_double(p):
    'array_con_valores_double : I_CORCHETE D_CORCHETE floating_type I_LLAVE valores_double D_LLAVE'

def p_array_con_valores_string(p):
    'array_con_valores_string : I_CORCHETE D_CORCHETE STRINGTYPE I_LLAVE valores_string D_LLAVE'

def p_array_con_valores_boolean(p):
    'array_con_valores_boolean : I_CORCHETE D_CORCHETE BOOLEAN I_LLAVE valores_boolean D_LLAVE'

def p_array_length_con_valores_int(p):
    'array_length_con_valores_int : array_length INTEGER I_LLAVE valores_int D_LLAVE'

def p_array_length_con_valores_double(p):
    'array_length_con_valores_double : array_length floating_type I_LLAVE valores_double D_LLAVE'

def p_array_length_con_valores_string(p):
    'array_length_con_valores_string : array_length STRINGTYPE I_LLAVE valores_string D_LLAVE'

def p_array_length_con_valores_boolean(p):
    'array_length_con_valores_boolean : array_length BOOLEAN I_LLAVE valores_boolean D_LLAVE'
# Fin de arreglo

# Definicion Variable por Daniel Torres

# def p_def_variable(p):
#     '''instruccion : def_varib '''
  
# Maps - Danny Loor
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
    '''init_struct : empty_struct ASIGNACION ID I_LLAVE valores D_LLAVE
                    | ID DECLARACION_ASIGNACION ID I_LLAVE valores D_LLAVE
                    | empty_struct ASIGNACION ID I_LLAVE atributos_nombrados D_LLAVE
                    | ID DECLARACION_ASIGNACION ID I_LLAVE atributos_nombrados D_LLAVE'''

def p_atributos_nombrados(p):
    '''atributos_nombrados : declara_atributo
                    | declara_atributo COMA atributos_nombrados'''

def p_valor_var_struct(p):
    'valor_struct : ID PUNTO ID'

def p_nombrandos_struct(p):
    '''declara_atributo : ID DOS_PUNTOS expression
                      | ID DOS_PUNTOS expression_bool'''

# Maps - Dannh Loor
def p_clave_valor(p):
    '''clave_valor : valor DOS_PUNTOS valor'''

def p_multiple_clave_valor(p):
    '''claves_valores : clave_valor
          | clave_valor COMA claves_valores'''


def p_condicion(p):
    '''condicion : expression_bool
                | I_PARENTESIS expression_bool D_PARENTESIS'''

# def p_iteracion_for(p):
#     'iteracion_for : ID'

def p_expression_bool(p):
    '''expression_bool : valor_boolean
                  | valor_variable
                  | resultado_bool
                  | llamada_func
                  | compare_expressions
                  | I_PARENTESIS resultado_bool D_PARENTESIS
                  | I_PARENTESIS compare_expressions D_PARENTESIS'''

def p_resultado_bool(p):
    '''resultado_bool : expression_bool operacion_binaria_logica expression_bool'''

def p_compare_express(p):
    '''compare_expressions : expression operacion_binaria_comparativa expression'''

def p_expression_term(p):
    '''expression : valor_int
                  | valor_double
                  | valor_variable
                  | resultado
                  | llamada_func
                  | I_PARENTESIS resultado D_PARENTESIS'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[2]

def p_expression_operation(p):
    'resultado : expression operacion_binaria_matematica expression'
    #Diego Arteaga
    var1 = p[3]
    var2 = p[1]
    # Esta condicion es para asignar el valor de la variable almacenada
    if var1 in booleanos or var2 in booleanos:
        return
    if var1 in variables:
        var1 = variables[var1]
    if var2 in variables:
        var2 = variables[var2]
    p[0] = str(operation(p[2], var2, var1))

def p_incremento_decremento(p):
    '''resultado_inc_dec : ID operador_matematico
                        | valor_struct operador_matematico'''
    
    #Diego Arteaga
    variable_inc_dec = p[1]
    # Esta condicion es para asignar el valor de la variable almacenada
    try:
        if variable_inc_dec in variables:
            variable_inc_dec = variables[variable_inc_dec]
        if (not variable_inc_dec.isdigit()) and variable_inc_dec.find(".") == -1:
            return
        variable_inc_dec = int(variable_inc_dec) if variable_inc_dec.find(".") == -1 else float(variable_inc_dec)
        if p[2] == '++':
            variables[p[1]] = variable_inc_dec + 1
        elif p[2] == '--':
            variables[p[1]] = variable_inc_dec - 1
        p[0] = str(variables[p[1]])
    except:
        raise AnalyzerException("ERROR: Error semántico en la operación de decremento e incremento: " + p)

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
  
# def p_operacion_mat(p):
#     'valor : valor operacion_binaria valor'

def p_print_options(p):
    '''print : PRINTLN
          | PRINTF
          | PRINT'''

def p_tipo_array(p):
    '''array_type_spec : array_length INTEGER
          | array_length STRINGTYPE
          | array_length BOOLEAN
          | array_length floating_type'''

def p_array_length_notype(p):
    'array_length : I_CORCHETE INT D_CORCHETE'

def p_tipo(p):
    '''type : BOOL
          | STRINGTYPE
          | INTEGER
          | floating_type'''

def p_tipo_flotante(p):
    ''' floating_type : FLOAT32
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

def p_mores_operaciones(p):
    '''operacion_binaria : operacion_binaria_comparativa
          | operacion_binaria_logica
          | operacion_binaria_matematica'''

def p_operacion_mat_simbolos(p):
    '''operacion_binaria_matematica : ADICION
          | RESTA
          | MULTIPLICACION
          | DIVISION
          | MODULO'''

def p_operacion_comp_simbolos(p):
    '''operacion_binaria_comparativa : MENOR_IGUAL
          | IGUAL
          | DIFERENTE
          | MAYOR
          | MAYOR_IGUAL
          | MENOR'''

def p_operacion_logica(p):
    '''operacion_binaria_logica : AND
          | OR'''

def p_valores(p):
    '''valor : valor_int
          | valor_double
          | valor_string
          | valor_boolean
          | valor_variable
          | valor_struct'''

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
    raise AnalyzerException("ERROR: Sintáxis no válida en la entrada!: " + p)


# Build the parser
parser_sem = sintactico.yacc()


def valida_regla(s):
    result = parser_sem.parse(s)
    print(result)
