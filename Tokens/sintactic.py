import ply.yacc as sintaxis
import practica
tokens = practica.tokens
#Ejemplos para probar con IF
#if $var==5 { echo 3; }
#if $var1!=$var2 { echo 'Ayer'; } else { date('Hoy'); }

def p_sentencias(p):
    '''sentencias : asignacion
    | expresion
    | metodos
    | if
    | for
    | while'''

def p_for(p):
    'for : LPAREN asignacion comparaciones PUNTOCOMA incremento_decremento RPAREN L_LLAVE sentencias R_LLAVE'

def p_while(p):
    'while : WHILE LPAREN comparaciones RPAREN L_LLAVE sentencias R_LLAVE'

def p_incremento_decremento_prein(p):
    'incremento_decremento : PREINCREMENTO VARIABLE'
def p_incremento_decremento_postin(p):
    'incremento_decremento : VARIABLE POSTINCREMENTO'
def p_incremento_decremento_prede(p):
    'incremento_decremento : PREDECREMENTO VARIABLE'

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

def p_asignacion(p):
    'asignacion : VARIABLE IGUAL expresion PUNTOCOMA'

def p_expresion_suma(p):
    'expresion : term operadores term'
def p_expresion_resta(p):
    'expresion : term operadores term expresion'

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
def p_noidentico_compare(p):
    'condiciones : factor NOIDENTICO factor'
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
def p_factor_var2(p):
    'factor : ID'
def p_factor_bool(p):
    'factor : BOOLEAN'
def p_factor_expr(p):
    'factor : LPAREN expresion RPAREN'
# Error generado
def p_error(p):
    print("Error de sintaxis:")
# Construir parser
parser = sintaxis.yacc()
while True:
    try:
        s = input('<php?> ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)
