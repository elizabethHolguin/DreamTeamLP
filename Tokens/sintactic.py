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
    'for : LPAREN asignacion VARIABLE condicion PUNTOCOMA incremento_decremento RPAREN L_LLAVE sentencias R_LLAVE'
def p_while(p):
    '''while : WHILE LPAREN condicion RPAREN L_LLAVE sentencias R_LLAVE
    | WHILE LPAREN condiciones RPAREN L_LLAVE sentencias R_LLAVE'''
def p_incremento_decremento(p):
    '''incremento_decremento : PREINCREMENTO VARIABLE
    | VARIABLE POSTINCREMENTO
    | PREDECREMENTO VARIABLE'''
def p_conver_object(p):
    'object : LPAREN OBJECT RPAREN term'
def p_metodos(p):
    '''metodos : imprimir
    | object'''
def p_imprimir(p):
    '''imprimir : ECHO factor PUNTOCOMA
    | PRINT LPAREN factor RPAREN PUNTOCOMA
    | PRINT factor '''
def p_if(p):
    '''if : IF LPAREN condiciones RPAREN L_LLAVE sentencias R_LLAVE
    | IF condiciones L_LLAVE sentencias R_LLAVE else
    | IF condiciones L_LLAVE sentencias R_LLAVE elseif else'''
def p_elseif(p):
    '''elseif : ELSEIF condicion L_LLAVE sentencias R_LLAVE
    | ELSEIF condiciones L_LLAVE sentencias R_LLAVE elseif'''
def p_else(p):
    'else : ELSE L_LLAVE sentencias R_LLAVE'
def p_asignacion(p):
    'asignacion : VARIABLE IGUAL expresion PUNTOCOMA'
def p_expresion_suma(p):
    'expresion : expresion MAS term'
def p_expresion_resta(p):
    'expresion : expresion MENOS term'
def p_expresion_producto(p):
    'expresion : expresion PRODUCTO term'
def p_expresion_division(p):
    'expresion : expresion DIVISION term'
def p_expresion_potencia(p):
    'expresion : expresion POTENCIA term'
def p_expresion_modulo(p):
    '''expresion : MODULO LPAREN NUMEROS COMA NUMEROS RPAREN
    | MODULO LPAREN NUMEROS COMA factorF RPAREN'''
def p_factor_float(p):
    'factorF : NUMEROS PUNTO NUMEROS'
def p_expression_term(p):
    'expresion : term'
def p_igualdad_compare(p):
    'condicion : factor IGUAL_IGUAL factor'
def p_identidad_compare(p):
    'condicion : factor IDENTICO factor'
def p_distinto_compare(p):
    'condicion : factor DISTINTO factor'
def p_noidentico_compare(p):
    'condicion : factor NOIDENTICO factor'
def p_menorque_compare(p):
    'condicion : factor MENORQUE factor'
def p_mayorque_compare(p):
    'condicion : factor MAYORQUE factor'
def p_menoroigual_compare(p):
    'condicion : factor MENOROIGUAL factor'
def p_mayoroigual_compare(p):
    'condicion : factor MAYOROIGUAL factor'
def p_condiciones(p):
    'condiciones : condicion'
def p_condiciones_xor(p):
    'condiciones : condiciones XOR condicion'
def p_condiciones_andand(p):
    'condiciones : condiciones ANDAND condicion'
def p_condiciones_and(p):
    'condiciones : condiciones AND condicion'
def p_condiciones_or(p):
    'condiciones : condiciones OR condicion'
def p_condiciones_oror(p):
    'condiciones : condiciones OROR condicion'
def p_term_factor(p):
    '''term : factor
    | factorF'''
def p_factor_num(p):
    'factor : NUMEROS'
def p_factor_str(p):
    '''factor : CADENASIMPLE
    | CADENADOBLE'''
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
