
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ADICION AND ASIGNACION ASIGNACION_ADICION ASIGNACION_DIVISION ASIGNACION_MODULO ASIGNACION_MULTI ASIGNACION_RESTA BOOL BOOLEAN BREAK CASE CHAN COMA CONST CONTINUE DECLARACION_ASIGNACION DECREMENTO DEFAULT DEFER DIFERENTE DIVISION DOS_PUNTOS DOUBLE D_CORCHETE D_LLAVE D_PARENTESIS ELSE ELSEIF FALLTHROUGH FLOAT32 FLOAT64 FOR FUNC GO GOTO ID IDENTIFICADOR IF IGUAL IMPORT INCREMENTO INT INTEGER INTERFACE I_CORCHETE I_LLAVE I_PARENTESIS MAKE MAP MAYOR MAYOR_IGUAL MENOR MENOR_IGUAL MODULO MULTIPLICACION NOT OR PACKAGE PRINT PRINTF PRINTLN PUNTO PUNTO_COMA RANGE RESTA RETURN SELECT STRING STRINGTYPE STRUCT SWITCH TYPE VARbody : instruccioninstruccion : print I_PARENTESIS valores D_PARENTESISinstruccion : VAR ID type ASIGNACION valor\n                   | VAR ID ASIGNACION valor\n                   | VAR ID ASIGNACION instruccioninstruccion : ID asignacion valor\n          | ID asignacion instruccioninstruccion : ID operador_matematicoinstruccion : IF condicion I_LLAVE body D_LLAVEinstruccion : ELSE I_LLAVE body D_LLAVEinstruccion : ELSEIF condicion I_LLAVE body D_LLAVEinstruccion : FOR ID DECLARACION_ASIGNACION RANGE ID I_LLAVE body D_LLAVEinstruccion : FOR instruccion PUNTO_COMA valor PUNTO_COMA ID operador_matematico I_LLAVE body D_LLAVEinstruccion : FOR ID COMA ID DECLARACION_ASIGNACION RANGE ID I_LLAVE body D_LLAVEinstruccion : I_CORCHETE D_CORCHETE type I_LLAVE D_LLAVEinstruccion : I_CORCHETE INT D_CORCHETE type I_LLAVE D_LLAVEinstruccion : I_CORCHETE D_CORCHETE type I_LLAVE valores D_LLAVEinstruccion : I_CORCHETE INT D_CORCHETE type I_LLAVE valores D_LLAVEinstruccion : MAP I_CORCHETE type D_CORCHETE type I_LLAVE D_LLAVEinstruccion : MAKE I_PARENTESIS MAP I_CORCHETE type D_CORCHETE type D_PARENTESISinstruccion : MAP I_CORCHETE type D_CORCHETE type I_LLAVE claves_valores D_LLAVEinstruccion : TYPE ID STRUCT I_LLAVE atributos D_LLAVEatributos : atributo\n                | atributo atributosatributo : ID typeinstruccion : init_structinit_struct : VAR ID ID ASIGNACION ID I_LLAVE valores D_LLAVE\n                    | ID DECLARACION_ASIGNACION ID I_LLAVE valores D_LLAVEclave_valor : valor DOS_PUNTOS valorclaves_valores : clave_valor\n          | clave_valor COMA claves_valorescondicion : valor\n                | I_PARENTESIS valor D_PARENTESISiteracion_for : ID valores : valor\n          | valor COMA valoresvalor : valor operacion_binaria valorprint : PRINTLN\n          | PRINTF\n          | PRINTtype : BOOL\n          | STRINGTYPE\n          | INTEGER\n          | FLOAT32\n          | FLOAT64operador_matematico : INCREMENTO\n          | DECREMENTOasignacion : ASIGNACION\n          | ASIGNACION_ADICION\n          | ASIGNACION_RESTA\n          | ASIGNACION_MULTI\n          | DECLARACION_ASIGNACION\n          | ASIGNACION_DIVISION\n          | ASIGNACION_MODULOoperacion_binaria : ADICION\n          | RESTA\n          | MULTIPLICACION\n          | DIVISION\n          | MODULOoperacion_binaria : MENOR_IGUAL\n          | IGUAL\n          | DIFERENTE\n          | MAYOR\n          | MAYOR_IGUAL\n          | MENORvalor : INT\n          | DOUBLE\n          | STRING\n          | ID'
    
_lr_action_items = {'VAR':([0,9,20,22,23,24,25,26,27,28,38,51,61,76,77,124,147,148,],[4,4,4,-52,-48,-49,-50,-51,-53,-54,4,4,4,4,-52,4,4,4,]),'ID':([0,4,6,8,9,13,18,19,20,22,23,24,25,26,27,28,33,38,51,52,53,54,55,56,61,62,63,64,65,66,67,68,69,70,71,72,73,76,77,78,79,86,87,88,91,97,100,104,113,116,121,122,124,125,130,132,147,148,150,151,],[5,19,37,37,40,46,37,49,57,60,-48,-49,-50,-51,-53,-54,37,5,57,-41,-42,-43,-44,-45,5,37,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,5,60,98,37,37,106,37,37,111,37,119,126,37,119,37,5,137,37,-25,5,5,37,37,]),'IF':([0,9,20,22,23,24,25,26,27,28,38,51,61,76,77,124,147,148,],[6,6,6,-52,-48,-49,-50,-51,-53,-54,6,6,6,6,-52,6,6,6,]),'ELSE':([0,9,20,22,23,24,25,26,27,28,38,51,61,76,77,124,147,148,],[7,7,7,-52,-48,-49,-50,-51,-53,-54,7,7,7,7,-52,7,7,7,]),'ELSEIF':([0,9,20,22,23,24,25,26,27,28,38,51,61,76,77,124,147,148,],[8,8,8,-52,-48,-49,-50,-51,-53,-54,8,8,8,8,-52,8,8,8,]),'FOR':([0,9,20,22,23,24,25,26,27,28,38,51,61,76,77,124,147,148,],[9,9,9,-52,-48,-49,-50,-51,-53,-54,9,9,9,9,-52,9,9,9,]),'I_CORCHETE':([0,9,11,20,22,23,24,25,26,27,28,38,51,61,76,77,83,124,147,148,],[10,10,44,10,-52,-48,-49,-50,-51,-53,-54,10,10,10,10,-52,103,10,10,10,]),'MAP':([0,9,20,22,23,24,25,26,27,28,38,45,51,61,76,77,124,147,148,],[11,11,11,-52,-48,-49,-50,-51,-53,-54,11,83,11,11,11,-52,11,11,11,]),'MAKE':([0,9,20,22,23,24,25,26,27,28,38,51,61,76,77,124,147,148,],[12,12,12,-52,-48,-49,-50,-51,-53,-54,12,12,12,12,-52,12,12,12,]),'TYPE':([0,9,20,22,23,24,25,26,27,28,38,51,61,76,77,124,147,148,],[13,13,13,-52,-48,-49,-50,-51,-53,-54,13,13,13,13,-52,13,13,13,]),'PRINTLN':([0,9,20,22,23,24,25,26,27,28,38,51,61,76,77,124,147,148,],[15,15,15,-52,-48,-49,-50,-51,-53,-54,15,15,15,15,-52,15,15,15,]),'PRINTF':([0,9,20,22,23,24,25,26,27,28,38,51,61,76,77,124,147,148,],[16,16,16,-52,-48,-49,-50,-51,-53,-54,16,16,16,16,-52,16,16,16,]),'PRINT':([0,9,20,22,23,24,25,26,27,28,38,51,61,76,77,124,147,148,],[17,17,17,-52,-48,-49,-50,-51,-53,-54,17,17,17,17,-52,17,17,17,]),'$end':([1,2,14,21,29,30,34,35,36,37,57,58,59,85,89,90,93,95,107,109,110,114,123,127,128,133,139,140,145,146,149,152,157,158,],[0,-1,-26,-8,-46,-47,-66,-67,-68,-69,-69,-6,-7,-2,-4,-5,-37,-10,-3,-9,-11,-15,-28,-17,-16,-22,-18,-19,-27,-12,-21,-20,-14,-13,]),'D_LLAVE':([2,14,21,29,30,34,35,36,37,48,52,53,54,55,56,57,58,59,75,85,89,90,92,93,95,96,100,105,107,108,109,110,114,115,116,120,121,123,127,128,129,130,132,133,134,135,136,139,140,141,142,145,146,149,152,153,154,155,156,157,158,],[-1,-26,-8,-46,-47,-66,-67,-68,-69,-35,-41,-42,-43,-44,-45,-69,-6,-7,95,-2,-4,-5,109,-37,-10,110,114,-36,-3,123,-9,-11,-15,127,128,133,-23,-28,-17,-16,139,140,-25,-22,-24,145,146,-18,-19,149,-30,-27,-12,-21,-20,157,158,-31,-29,-14,-13,]),'I_PARENTESIS':([3,6,8,12,15,16,17,],[18,33,33,45,-38,-39,-40,]),'DECLARACION_ASIGNACION':([5,40,57,98,],[22,77,22,112,]),'ASIGNACION':([5,19,40,49,50,52,53,54,55,56,57,],[23,51,23,87,88,-41,-42,-43,-44,-45,23,]),'ASIGNACION_ADICION':([5,40,57,],[24,24,24,]),'ASIGNACION_RESTA':([5,40,57,],[25,25,25,]),'ASIGNACION_MULTI':([5,40,57,],[26,26,26,]),'ASIGNACION_DIVISION':([5,40,57,],[27,27,27,]),'ASIGNACION_MODULO':([5,40,57,],[28,28,28,]),'INCREMENTO':([5,40,57,126,],[29,29,29,29,]),'DECREMENTO':([5,40,57,126,],[30,30,30,30,]),'INT':([6,8,10,18,20,22,23,24,25,26,27,28,33,51,62,63,64,65,66,67,68,69,70,71,72,73,77,79,86,88,91,100,116,122,130,150,151,],[34,34,43,34,34,-52,-48,-49,-50,-51,-53,-54,34,34,34,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-52,34,34,34,34,34,34,34,34,34,34,]),'DOUBLE':([6,8,18,20,22,23,24,25,26,27,28,33,51,62,63,64,65,66,67,68,69,70,71,72,73,77,79,86,88,91,100,116,122,130,150,151,],[35,35,35,35,-52,-48,-49,-50,-51,-53,-54,35,35,35,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-52,35,35,35,35,35,35,35,35,35,35,]),'STRING':([6,8,18,20,22,23,24,25,26,27,28,33,51,62,63,64,65,66,67,68,69,70,71,72,73,77,79,86,88,91,100,116,122,130,150,151,],[36,36,36,36,-52,-48,-49,-50,-51,-53,-54,36,36,36,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-52,36,36,36,36,36,36,36,36,36,36,]),'I_LLAVE':([7,29,30,31,32,34,35,36,37,39,52,53,54,55,56,60,80,84,93,94,101,106,111,117,137,138,],[38,-46,-47,61,-32,-66,-67,-68,-69,76,-41,-42,-43,-44,-45,91,100,104,-37,-33,116,122,124,130,147,148,]),'D_CORCHETE':([10,43,52,53,54,55,56,82,118,],[42,81,-41,-42,-43,-44,-45,102,131,]),'PUNTO_COMA':([14,21,29,30,34,35,36,37,41,57,58,59,85,89,90,93,95,99,107,109,110,114,123,127,128,133,139,140,145,146,149,152,157,158,],[-26,-8,-46,-47,-66,-67,-68,-69,79,-69,-6,-7,-2,-4,-5,-37,-10,113,-3,-9,-11,-15,-28,-17,-16,-22,-18,-19,-27,-12,-21,-20,-14,-13,]),'BOOL':([19,42,44,81,102,103,119,131,],[52,52,52,52,52,52,52,52,]),'STRINGTYPE':([19,42,44,81,102,103,119,131,],[53,53,53,53,53,53,53,53,]),'INTEGER':([19,42,44,81,102,103,119,131,],[54,54,54,54,54,54,54,54,]),'FLOAT32':([19,42,44,81,102,103,119,131,],[55,55,55,55,55,55,55,55,]),'FLOAT64':([19,42,44,81,102,103,119,131,],[56,56,56,56,56,56,56,56,]),'ADICION':([32,34,35,36,37,48,57,58,74,89,93,99,107,143,156,],[63,-66,-67,-68,-69,63,-69,63,63,63,63,63,63,63,63,]),'RESTA':([32,34,35,36,37,48,57,58,74,89,93,99,107,143,156,],[64,-66,-67,-68,-69,64,-69,64,64,64,64,64,64,64,64,]),'MULTIPLICACION':([32,34,35,36,37,48,57,58,74,89,93,99,107,143,156,],[65,-66,-67,-68,-69,65,-69,65,65,65,65,65,65,65,65,]),'DIVISION':([32,34,35,36,37,48,57,58,74,89,93,99,107,143,156,],[66,-66,-67,-68,-69,66,-69,66,66,66,66,66,66,66,66,]),'MODULO':([32,34,35,36,37,48,57,58,74,89,93,99,107,143,156,],[67,-66,-67,-68,-69,67,-69,67,67,67,67,67,67,67,67,]),'MENOR_IGUAL':([32,34,35,36,37,48,57,58,74,89,93,99,107,143,156,],[68,-66,-67,-68,-69,68,-69,68,68,68,68,68,68,68,68,]),'IGUAL':([32,34,35,36,37,48,57,58,74,89,93,99,107,143,156,],[69,-66,-67,-68,-69,69,-69,69,69,69,69,69,69,69,69,]),'DIFERENTE':([32,34,35,36,37,48,57,58,74,89,93,99,107,143,156,],[70,-66,-67,-68,-69,70,-69,70,70,70,70,70,70,70,70,]),'MAYOR':([32,34,35,36,37,48,57,58,74,89,93,99,107,143,156,],[71,-66,-67,-68,-69,71,-69,71,71,71,71,71,71,71,71,]),'MAYOR_IGUAL':([32,34,35,36,37,48,57,58,74,89,93,99,107,143,156,],[72,-66,-67,-68,-69,72,-69,72,72,72,72,72,72,72,72,]),'MENOR':([32,34,35,36,37,48,57,58,74,89,93,99,107,143,156,],[73,-66,-67,-68,-69,73,-69,73,73,73,73,73,73,73,73,]),'COMA':([34,35,36,37,40,48,93,142,156,],[-66,-67,-68,-69,78,86,-37,150,-29,]),'D_PARENTESIS':([34,35,36,37,47,48,52,53,54,55,56,74,93,105,144,],[-66,-67,-68,-69,85,-35,-41,-42,-43,-44,-45,94,-37,-36,152,]),'DOS_PUNTOS':([34,35,36,37,93,143,],[-66,-67,-68,-69,-37,151,]),'STRUCT':([46,],[84,]),'RANGE':([77,112,],[97,125,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'body':([0,38,61,76,124,147,148,],[1,75,92,96,136,153,154,]),'instruccion':([0,9,20,38,51,61,76,124,147,148,],[2,41,59,2,90,2,2,2,2,2,]),'print':([0,9,20,38,51,61,76,124,147,148,],[3,3,3,3,3,3,3,3,3,3,]),'init_struct':([0,9,20,38,51,61,76,124,147,148,],[14,14,14,14,14,14,14,14,14,14,]),'asignacion':([5,40,57,],[20,20,20,]),'operador_matematico':([5,40,57,126,],[21,21,21,138,]),'condicion':([6,8,],[31,39,]),'valor':([6,8,18,20,33,51,62,79,86,88,91,100,116,122,130,150,151,],[32,32,48,58,74,89,93,99,48,107,48,48,48,48,143,143,156,]),'valores':([18,86,91,100,116,122,],[47,105,108,115,129,135,]),'type':([19,42,44,81,102,103,119,131,],[50,80,82,101,117,118,132,144,]),'operacion_binaria':([32,48,58,74,89,93,99,107,143,156,],[62,62,62,62,62,62,62,62,62,62,]),'atributos':([104,121,],[120,134,]),'atributo':([104,121,],[121,121,]),'claves_valores':([130,150,],[141,155,]),'clave_valor':([130,150,],[142,142,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> body","S'",1,None,None,None),
  ('body -> instruccion','body',1,'p_body','sintactico.py',18),
  ('instruccion -> print I_PARENTESIS valores D_PARENTESIS','instruccion',4,'p_impresion','sintactico.py',21),
  ('instruccion -> VAR ID type ASIGNACION valor','instruccion',5,'p_declaracion','sintactico.py',24),
  ('instruccion -> VAR ID ASIGNACION valor','instruccion',4,'p_declaracion','sintactico.py',25),
  ('instruccion -> VAR ID ASIGNACION instruccion','instruccion',4,'p_declaracion','sintactico.py',26),
  ('instruccion -> ID asignacion valor','instruccion',3,'p_asignacion','sintactico.py',29),
  ('instruccion -> ID asignacion instruccion','instruccion',3,'p_asignacion','sintactico.py',30),
  ('instruccion -> ID operador_matematico','instruccion',2,'p_incremento_decremento','sintactico.py',33),
  ('instruccion -> IF condicion I_LLAVE body D_LLAVE','instruccion',5,'p_if_condicion','sintactico.py',38),
  ('instruccion -> ELSE I_LLAVE body D_LLAVE','instruccion',4,'p_else_condicion','sintactico.py',41),
  ('instruccion -> ELSEIF condicion I_LLAVE body D_LLAVE','instruccion',5,'p_if_else_condicion','sintactico.py',44),
  ('instruccion -> FOR ID DECLARACION_ASIGNACION RANGE ID I_LLAVE body D_LLAVE','instruccion',8,'p_for_each','sintactico.py',47),
  ('instruccion -> FOR instruccion PUNTO_COMA valor PUNTO_COMA ID operador_matematico I_LLAVE body D_LLAVE','instruccion',10,'p_for_condicion','sintactico.py',50),
  ('instruccion -> FOR ID COMA ID DECLARACION_ASIGNACION RANGE ID I_LLAVE body D_LLAVE','instruccion',10,'p_for_map','sintactico.py',53),
  ('instruccion -> I_CORCHETE D_CORCHETE type I_LLAVE D_LLAVE','instruccion',5,'p_array','sintactico.py',58),
  ('instruccion -> I_CORCHETE INT D_CORCHETE type I_LLAVE D_LLAVE','instruccion',6,'p_array_length','sintactico.py',61),
  ('instruccion -> I_CORCHETE D_CORCHETE type I_LLAVE valores D_LLAVE','instruccion',6,'p_array_con_valores','sintactico.py',64),
  ('instruccion -> I_CORCHETE INT D_CORCHETE type I_LLAVE valores D_LLAVE','instruccion',7,'p_array_length_con_valores','sintactico.py',67),
  ('instruccion -> MAP I_CORCHETE type D_CORCHETE type I_LLAVE D_LLAVE','instruccion',7,'p_map','sintactico.py',70),
  ('instruccion -> MAKE I_PARENTESIS MAP I_CORCHETE type D_CORCHETE type D_PARENTESIS','instruccion',8,'p_map_make','sintactico.py',73),
  ('instruccion -> MAP I_CORCHETE type D_CORCHETE type I_LLAVE claves_valores D_LLAVE','instruccion',8,'p_map_valores','sintactico.py',76),
  ('instruccion -> TYPE ID STRUCT I_LLAVE atributos D_LLAVE','instruccion',6,'p_struct','sintactico.py',79),
  ('atributos -> atributo','atributos',1,'p_atributos','sintactico.py',82),
  ('atributos -> atributo atributos','atributos',2,'p_atributos','sintactico.py',83),
  ('atributo -> ID type','atributo',2,'p_atributo','sintactico.py',86),
  ('instruccion -> init_struct','instruccion',1,'p_declaracion_struct','sintactico.py',89),
  ('init_struct -> VAR ID ID ASIGNACION ID I_LLAVE valores D_LLAVE','init_struct',8,'p_init_struct','sintactico.py',92),
  ('init_struct -> ID DECLARACION_ASIGNACION ID I_LLAVE valores D_LLAVE','init_struct',6,'p_init_struct','sintactico.py',93),
  ('clave_valor -> valor DOS_PUNTOS valor','clave_valor',3,'p_clave_valor','sintactico.py',96),
  ('claves_valores -> clave_valor','claves_valores',1,'p_multiple_clave_valor','sintactico.py',99),
  ('claves_valores -> clave_valor COMA claves_valores','claves_valores',3,'p_multiple_clave_valor','sintactico.py',100),
  ('condicion -> valor','condicion',1,'p_condicion','sintactico.py',103),
  ('condicion -> I_PARENTESIS valor D_PARENTESIS','condicion',3,'p_condicion','sintactico.py',104),
  ('iteracion_for -> ID','iteracion_for',1,'p_iteracion_for','sintactico.py',107),
  ('valores -> valor','valores',1,'p_multiples_valores','sintactico.py',118),
  ('valores -> valor COMA valores','valores',3,'p_multiples_valores','sintactico.py',119),
  ('valor -> valor operacion_binaria valor','valor',3,'p_operacion_mat','sintactico.py',122),
  ('print -> PRINTLN','print',1,'p_print_options','sintactico.py',125),
  ('print -> PRINTF','print',1,'p_print_options','sintactico.py',126),
  ('print -> PRINT','print',1,'p_print_options','sintactico.py',127),
  ('type -> BOOL','type',1,'p_tipo','sintactico.py',130),
  ('type -> STRINGTYPE','type',1,'p_tipo','sintactico.py',131),
  ('type -> INTEGER','type',1,'p_tipo','sintactico.py',132),
  ('type -> FLOAT32','type',1,'p_tipo','sintactico.py',133),
  ('type -> FLOAT64','type',1,'p_tipo','sintactico.py',134),
  ('operador_matematico -> INCREMENTO','operador_matematico',1,'p_operacion_mat_var','sintactico.py',137),
  ('operador_matematico -> DECREMENTO','operador_matematico',1,'p_operacion_mat_var','sintactico.py',138),
  ('asignacion -> ASIGNACION','asignacion',1,'p_operadores_asignacion','sintactico.py',141),
  ('asignacion -> ASIGNACION_ADICION','asignacion',1,'p_operadores_asignacion','sintactico.py',142),
  ('asignacion -> ASIGNACION_RESTA','asignacion',1,'p_operadores_asignacion','sintactico.py',143),
  ('asignacion -> ASIGNACION_MULTI','asignacion',1,'p_operadores_asignacion','sintactico.py',144),
  ('asignacion -> DECLARACION_ASIGNACION','asignacion',1,'p_operadores_asignacion','sintactico.py',145),
  ('asignacion -> ASIGNACION_DIVISION','asignacion',1,'p_operadores_asignacion','sintactico.py',146),
  ('asignacion -> ASIGNACION_MODULO','asignacion',1,'p_operadores_asignacion','sintactico.py',147),
  ('operacion_binaria -> ADICION','operacion_binaria',1,'p_operacion_mat_simbolos','sintactico.py',150),
  ('operacion_binaria -> RESTA','operacion_binaria',1,'p_operacion_mat_simbolos','sintactico.py',151),
  ('operacion_binaria -> MULTIPLICACION','operacion_binaria',1,'p_operacion_mat_simbolos','sintactico.py',152),
  ('operacion_binaria -> DIVISION','operacion_binaria',1,'p_operacion_mat_simbolos','sintactico.py',153),
  ('operacion_binaria -> MODULO','operacion_binaria',1,'p_operacion_mat_simbolos','sintactico.py',154),
  ('operacion_binaria -> MENOR_IGUAL','operacion_binaria',1,'p_operacion_comp_simbolos','sintactico.py',157),
  ('operacion_binaria -> IGUAL','operacion_binaria',1,'p_operacion_comp_simbolos','sintactico.py',158),
  ('operacion_binaria -> DIFERENTE','operacion_binaria',1,'p_operacion_comp_simbolos','sintactico.py',159),
  ('operacion_binaria -> MAYOR','operacion_binaria',1,'p_operacion_comp_simbolos','sintactico.py',160),
  ('operacion_binaria -> MAYOR_IGUAL','operacion_binaria',1,'p_operacion_comp_simbolos','sintactico.py',161),
  ('operacion_binaria -> MENOR','operacion_binaria',1,'p_operacion_comp_simbolos','sintactico.py',162),
  ('valor -> INT','valor',1,'p_valores','sintactico.py',165),
  ('valor -> DOUBLE','valor',1,'p_valores','sintactico.py',166),
  ('valor -> STRING','valor',1,'p_valores','sintactico.py',167),
  ('valor -> ID','valor',1,'p_valores','sintactico.py',168),
]
