import ply.yacc as sintaxis
import practica
tokens = practica.tokens
#Ejemplos para probar con IF
#if $var==5 { echo 3; }
#if $var1!=$var2 { echo 'Ayer'; } else { date('Hoy'); }

#ejemplos Kevin
#for($a=3;$a<4;$a++){$a=4;}
#while($a<4 && $b>5){$a++;}
#if($a<$b){print(5);}
#if($a<$b){print(5);}else{$a= 5+5;}
#if($a<$b){print(5);}elseif($a>4 || $b<4){$a="hola mundo1";}else{$a= 5+5;}

def p_sentencias(p):
    '''sentencias : asignacion
    | metodos
    | if
    | for
    | while'''

def p_for(p):
    'for : FOR LPAREN asignacion comparaciones PUNTOCOMA incremento_decremento RPAREN L_LLAVE sentencias R_LLAVE'

def p_while(p):
    'while : WHILE LPAREN comparaciones RPAREN L_LLAVE sentencias R_LLAVE'

def p_incremento_decremento_prein(p):
    'incremento_decremento : PREINCREMENTO'
def p_incremento_decremento_postin(p):
    'incremento_decremento : POSTINCREMENTO'
def p_incremento_decremento_prede(p):
    'incremento_decremento : PREDECREMENTO'
def p_incremento_decremento_postde(p):
    'incremento_decremento : POSTDECREMENTO'
def p_conver_object(p):
    'object : LPAREN OBJECT RPAREN term'

def p_metodos(p):
    '''metodos : imprimir
    | object
    | potencia'''
def p_imprimir_uno(p):
    'imprimir : ECHO factor PUNTOCOMA'
def p_imprimir_dos(p):
    'imprimir : PRINT LPAREN factor RPAREN PUNTOCOMA'
def p_imprimir_tres(p):
    'imprimir : PRINT factor'
def p_potencia(p):
    'potencia : POTENCIA LPAREN NUMEROS COMA NUMEROS RPAREN'

def p_if(p):
    'if : IF LPAREN comparaciones RPAREN L_LLAVE sentencias R_LLAVE'
def p_if_else(p):
    'if : IF LPAREN comparaciones RPAREN L_LLAVE sentencias R_LLAVE else'
def p_if_elseif(p):
    'if : IF LPAREN comparaciones RPAREN L_LLAVE sentencias R_LLAVE elseif else'

def p_elseif(p):
    'elseif : ELSEIF LPAREN comparaciones RPAREN L_LLAVE sentencias R_LLAVE'
def p_elseif_dos(p):
    'elseif : ELSEIF LPAREN comparaciones RPAREN L_LLAVE sentencias R_LLAVE elseif'

def p_else(p):
    'else : ELSE L_LLAVE sentencias R_LLAVE'

def p_asignacion_uno(p):
    'asignacion : VARIABLE IGUAL expresion PUNTOCOMA'
def p_asignacion_dos(p):
    'asignacion : VARIABLE IGUAL factor PUNTOCOMA'
def p_asignacion_incredecre(p):
    'asignacion : incremento_decremento PUNTOCOMA'

def p_expresion_uno(p):
    'expresion : term operadores term'
def p_expresion_dos(p):
    'expresion : expresion term operadores term'

def p_operadores_mas(p):
    'operadores : MAS'
def p_operadores_menos(p):
    'operadores : MENOS'
def p_operadores_producto(p):
    'operadores : PRODUCTO'
def p_operadores_division(p):
    'operadores : DIVISION'
def p_operadores_modulo(p):
    'operadores : MODULO'
def p_operadores_exponenciacion(p):
    'operadores : EXPONENCIACION'

def p_comparacion(p):
    'comparacion : condiciones'
def p_comparaciones_paren(p):
    'comparacion : LPAREN condiciones RPAREN'
def p_comparaciones_negado(p):
    'comparacion : NO LPAREN condiciones RPAREN'

def p_igualdad_compare(p):
    'condiciones : factor IGUAL_IGUAL factor'
def p_identidad_compare(p):
    'condiciones : factor IDENTICO factor'
def p_distinto_compare(p):
    'condiciones : factor DISTINTO factor'
def p_menorque_compare(p):
    'condiciones : factor MENORQUE factor'
def p_mayorque_compare(p):
    'condiciones : factor MAYORQUE factor'
def p_menoroigual_compare(p):
    'condiciones : factor MENOROIGUAL factor'
def p_mayoroigual_compare(p):
    'condiciones : factor MAYOROIGUAL factor'

def p_comparaciones(p):
    'comparaciones : comparacion'
def p_comparaciones_uno(p):
    'comparaciones : comparacion anado comparaciones'

def p_condicion_extra(p):
    'anado : condicion'

def p_condicion_xor(p):
    'condicion : XOR'
def p_condicion_andand(p):
    'condicion : ANDAND'
def p_condicion_and(p):
    'condicion : AND'
def p_condicion_or(p):
    'condicion : OR'
def p_condicion_oror(p):
    'condicion : OROR'

def p_term_factor(p):
    'term : factor'
def p_factor_num(p):
    'factor : NUMEROS'
def p_factor_float(p):
    'factor : NUMEROS PUNTO NUMEROS'
def p_factor_strsimple(p):
    'factor : CADENASIMPLE'
def p_factor_strdoble(p):
    'factor : CADENADOBLE'

def p_factor_var(p):
    'factor : VARIABLE'
def p_factor_bool(p):
    'factor : BOOLEAN'
def p_factor_expr(p):
    'factor : LPAREN expresion RPAREN'

def p_fopen(p):
    'fopen : LPAREN URL COMA MODOESCRITURA RPAREN PUNTOCOMA'

def p_fpassthru(p):
    'fpassthru : LPAREN VAR RPAREN PUNTOCOMA'

def p_feof(p):
    'feof : LPAREN VARIABLE RPAREN PUNTOCOMA'

def p_fgets(p):
    '''fgets : LPAREN VARIABLE COMA NUMEROS RPAREN
    |LPAREN VARIABLE RPAREN'''

def p_nl2br(p):
    '''nl2br : LPAREN CADENADOBLE RPAREN PUNTOCOMA
    |LPAREN CADENADOBLE COMA BOOLEAN RPAREN PUNTOCOMA
    |LPAREN VARIABLE RPAREN PUNTOCOMA
    |LPAREN CADENASIMPLE RPAREN PUNTOCOMA'''

def p_round(p):
    '''round : LPAREN DECIMAL RPAREN PUNTOCOMA
    |LPAREN MENOS DECIMAL RPAREN PUNTOCOMA
    |LPAREN DECIMAL COMA NUMEROS RPAREN PUNTOCOMA
    |LPAREN DECIMAL COMA MENOS NUMEROS RPAREN PUNTOCOMA
    |LPAREN MENOS DECIMAL COMA MENOS NUMEROS RPAREN PUNTOCOMA
    |LPAREN MENOS DECIMAL COMA NUMEROS RPAREN PUNTOCOMA
    |LPAREN MENOS DECIMAL COMA NUMEROS COMA PHP_ROUND_HALF_DOWN RPAREN PUNTOCOMA
    |LPAREN DECIMAL COMA NUMEROS COMA PHP_ROUND_HALF_DOWN RPAREN PUNTOCOMA'''

def p_floor(p):
    '''floor : LPAREN DECIMAL RPAREN PUNTOCOMA
    |LPAREN MENOS DECIMAL RPAREN PUNTOCOMA
    |LPAREN DECIMAL PRODUCTO NUMEROS RPAREN PUNTOCOMA
    |LPAREN VARIABLE RPAREN PUNTOCOMA'''

def p_ceil(p):
    '''ceil : LPAREN DECIMAL RPAREN PUNTOCOMA
    |LPAREN MENOS DECIMAL RPAREN PUNTOCOMA
    |LPAREN VARIABLE RPAREN PUNTOCOMA
    |LPAREN VARIABLE PRODUCTO NUMEROS RPAREN PUNTOCOMA'''

def p_list(p):
    'list : LPAREN VARIABLE COMA VARIABLE COMA VARIABLE RPAREN IGUAL VARIABLE PUNTOCOMA'


# Error generado
def p_error(p):
    if p:
        print("Error de sintaxis antes del '%s'" % p.value)
    else:
        print("Error de definicion")

#Construir parser
parser = sintaxis.yacc()

while True:
    try:
        s = input('<php?> ')
    except EOFError:
        break
    if not s:
        continue
    result = parser.parse(s)
    print(result)
