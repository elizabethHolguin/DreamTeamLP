import ply.yacc as sintaxis
import practica
tokens = practica.tokens

def p_sentencias(p):
    '''sentencias : sentencias asignacion
    | sentencias metodos
    | sentencias if
    | sentencias for
    | sentencias while
    | asignacion
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
    | object'''
def p_imprimir_uno(p):
    'imprimir : ECHO factor PUNTOCOMA'
def p_imprimir_unoA(p):
    'imprimir : ECHO funciones PUNTOCOMA'
def p_imprimir_dos(p):
    'imprimir : PRINT LPAREN factor RPAREN PUNTOCOMA'
def p_imprimir_dosA(p):
    'imprimir : PRINT LPAREN funciones RPAREN PUNTOCOMA'
def p_imprimir_tres(p):
    'imprimir : PRINT factor'
def p_imprimir_tresA(p):
    'imprimir : PRINT funciones'


def p_if(p):
    'if : IF LPAREN comparaciones RPAREN L_LLAVE sentencias R_LLAVE'
def p_if_else(p):
    'if : IF LPAREN comparaciones RPAREN L_LLAVE sentencias R_LLAVE else'
def p_if_elseif(p):
    'if : IF LPAREN comparaciones RPAREN L_LLAVE sentencias R_LLAVE elseif else'

def p_elseif(p):
    'elseif : ELSEIF LPAREN comparaciones RPAREN L_LLAVE sentencias R_LLAVE'
def p_elseif_dos(p):
    'elseif : elseif ELSEIF LPAREN comparaciones RPAREN L_LLAVE sentencias R_LLAVE'

def p_else(p):
    'else : ELSE L_LLAVE sentencias R_LLAVE'

def p_asignacion_uno(p):
    'asignacion : VARIABLE IGUAL expresion PUNTOCOMA'
def p_asignacion_dos(p):
    'asignacion : VARIABLE IGUAL factor PUNTOCOMA'
def p_asignacion_incredecre(p):
    'asignacion : incremento_decremento PUNTOCOMA'
def p_asignacion_funcion(p):
    'asignacion : VARIABLE IGUAL funciones PUNTOCOMA'

def p_expresion_uno(p):
    'expresion : expresion operadores term'
def p_expresion_dos(p):
    'expresion : term'

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
    'comparaciones : comparaciones anado comparacion'

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
    'factor : DECIMAL'
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
    '''fopen : FOPEN LPAREN CADENADOBLE COMA CADENADOBLE RPAREN
    | FOPEN LPAREN CADENASIMPLE COMA CADENADOBLE RPAREN'''

def p_fpassthru(p):
    'fpassthru : FPASSTHRU LPAREN VARIABLE RPAREN'

def p_feof(p):
    'feof : FEOF LPAREN VARIABLE RPAREN '

def p_fgets(p):
    '''fgets : FGETS LPAREN VARIABLE COMA NUMEROS RPAREN
    | FGETS LPAREN VARIABLE RPAREN'''

def p_nl2br(p):
    '''nl2br : NL2BR LPAREN CADENADOBLE COMA VARIABLE RPAREN
    | NL2BR LPAREN CADENADOBLE COMA BOOLEAN RPAREN
    | NL2BR LPAREN CADENADOBLE RPAREN
    | NL2BR LPAREN VARIABLE COMA BOOLEAN RPAREN
    | NL2BR LPAREN VARIABLE COMA VARIABLE RPAREN
    | NL2BR LPAREN VARIABLE RPAREN'''

def p_round(p):
    '''round : ROUND LPAREN DECIMAL RPAREN
    | ROUND LPAREN MENOS DECIMAL RPAREN
    | ROUND LPAREN DECIMAL COMA NUMEROS RPAREN
    | ROUND LPAREN DECIMAL COMA MENOS NUMEROS RPAREN
    | ROUND LPAREN MENOS DECIMAL COMA MENOS NUMEROS RPAREN
    | ROUND LPAREN MENOS DECIMAL COMA NUMEROS RPAREN'''

def p_floor(p):
    '''floor : FLOOR LPAREN DECIMAL RPAREN
    | FLOOR LPAREN MENOS DECIMAL RPAREN
    | FLOOR LPAREN DECIMAL PRODUCTO NUMEROS RPAREN
    | FLOOR LPAREN VARIABLE RPAREN'''

def p_ceil_1(p):
    'ceil : CEIL LPAREN MENOS DECIMAL RPAREN'
def p_ceil_2(p):
    'ceil : CEIL LPAREN DECIMAL RPAREN'
def p_ceil_3(p):
    'ceil : CEIL LPAREN VARIABLE RPAREN'
def p_ceil_4(p):
    'ceil : CEIL LPAREN VARIABLE PRODUCTO NUMEROS RPAREN'

def p_fmod(p):
    'fmod : FMOD LPAREN VARIABLE COMA VARIABLE RPAREN'


#RESOLVER
def p_lista(p):
    'lista : LIST LPAREN elements RPAREN'
def p_parte_lista_uno(p):
    'elements : factor'
def p_parte_lista_dos(p):
    'elements : element'
def p_parte_lista_tres(p):
    'elements : elements COMA factor'
def p_parte_lista_cuatro(p):
    'elements : elements COMA element'

def p_element(p):
    '''element : arrays
    | lista'''

def p_max_funcion(p):
    'max : MAX LPAREN elements RPAREN'

def p_arrays(p):
    '''arrays : ARRAY LPAREN elements RPAREN
    | LCORC elements RCORC'''

def p_min_funcion(p):
    'min : MIN LPAREN elements RPAREN'

def p_number_format_1(p):
    'number_format : NUMBER_FORMAT LPAREN VARIABLE RPAREN'

def p_number_format_2(p):
    'number_format : NUMBER_FORMAT LPAREN VARIABLE COMA NUMEROS RPAREN'

def p_number_format_4(p):
    'number_format : NUMBER_FORMAT LPAREN VARIABLE COMA NUMEROS COMA CADENASIMPLE COMA CADENASIMPLE RPAREN'

def p_funciones_s(p):
    '''funciones : trim
    | substr
    | wordwrap
    | fopen
    | fpassthru
    | feof
    | fgets
    | nl2br'''

def p_funciones_a(p):
    '''funciones : VARIABLE IGUAL next
    | lista
    | arrays'''
def p_rand_uno(p):
    'rand : RAND LPAREN NUMEROS COMA NUMEROS RPAREN'
def p_rand_dos(p):
    'rand : RAND LPAREN RPAREN'
def p_potencia(p):
    'funciones : POTENCIA LPAREN NUMEROS COMA NUMEROS RPAREN'

def p_funciones_i(p):
    '''funciones : max
    | min
    | sort
    | count
    | number_format
    | floor
    | round
    | ceil
    | rand
    | fmod'''

def p_trim_1(p):
    'trim : TRIM LPAREN VARIABLE RPAREN'

def p_trim_2(p):
    '''trim : TRIM LPAREN VARIABLE COMA CADENADOBLE RPAREN
    | TRIM LPAREN VARIABLE COMA CADENASIMPLE RPAREN'''

def p_substr_uno(p):
    'substr : SUBSTR LPAREN VARIABLE COMA NUMEROS COMA NUMEROS RPAREN'
def p_substr_dos(p):
    'substr : SUBSTR LPAREN CADENADOBLE COMA NUMEROS COMA NUMEROS RPAREN'
def p_substr_tres(p):
    'substr : SUBSTR LPAREN VARIABLE COMA NUMEROS RPAREN'
def p_substr_cuatro(p):
    'substr : SUBSTR LPAREN CADENADOBLE COMA NUMEROS RPAREN'

def p_wordwrap(p):
    'wordwrap : WORDWRAP LPAREN VARIABLE COMA NUMEROS COMA CADENADOBLE COMA BOOLEAN RPAREN'

def p_sort(p):
    'sort : SORT LPAREN VARIABLE RPAREN'

def p_sort_2(p):
    'sort : SORT LPAREN VARIABLE COMA FLAG RPAREN'

def p_count(p):
    'count : COUNT LPAREN VARIABLE RPAREN'

def p_next(p):
    'next : NEXT LPAREN VARIABLE RPAREN'

def p_funciones_obj(p):
    '''funciones : getclass
    | is_a'''
def p_getclass(p):
    'getclass : GETCLASS LPAREN VARIABLE RPAREN'
def p_is_a(p):
    'is_a : IS_A LPAREN VARIABLE COMA CADENADOBLE RPAREN'

# Error generado
def p_error(p):
    global bandera
    if p:
        print("Error de sintaxis en la linea: ", p.lineno, " posicion ", p.lexpos, "de tipo ", p.type)
        bandera = False
    else:
        print("Error de definicion")
        bandera = False
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

#Ejemplos para probar con IF
#if $var==5 { echo 3; }
#if $var1!=$var2 { echo 'Ayer'; } else { date('Hoy'); }

#ejemplos Kevin
#for($a=3;$a<4;$a++){$a=4;}
#while($a<4 && $b>5){$a++;}
#if($a<$b){print(5);}
#if($a<$b){print(5);}else{$a= 5+5;}
#if($a<$b){print(5);}elseif($a>4 || $b<4){$a="hola mundo1";}else{$a= 5+5;}

#EJEMPLOS DAVID
# $VAR = ["foo", "bar", "bar", "foo"];
# $VAR1 = sort($VAR);
# $VAR2 = trim($TELEFONO);
# $VAR3 = count($VAR1);

#EJEMPLOS JOSELYN
#echo floor(-5.46);
#print nl2br("foo no es bar");
#$x = round(5.6);
#$variable = fopen("c:\\folder\\resource.txt", "r");

#Algoritmo completo
#print("hola mundo");while($a<4 && $b>5){echo floor(-5.46);if($a<$b){$VAR = ["foo", "bar", "bar", "foo"]; echo "hola";}elseif($a>4 || $b<4){$a="hola mundo1"; echo $a;}else{for($a=3;$a<4;$a++){$a=4;$a++;}}}
