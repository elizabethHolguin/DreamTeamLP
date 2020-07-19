import ply.lex as lex

reserved = {'or': 'OR',
            'xor': 'XOR',
            'and': 'AND',
            'if': 'IF',
            'else': 'ELSE',
            'while': 'WHILE',
            'for': 'FOR',
            'echo': 'ECHO',
            'print':'PRINT',
            'array': 'ARRAY',
            'elseif': 'ELSEIF',
            'list': 'LIST',
            'boolean': 'BOOLEAN',
            'fopen': "FOPEN",
            'fpassthru': 'FPASSTHRU',
            'feof': 'FEOF',
            'fgets': 'FGETS',
            'nl2br': 'NL2BR',
            'round': 'ROUND',
            'floor': 'FLOOR',
            'ceil': 'CEIL',
            'potencia': 'POTENCIA',
            'max': 'MAX',
            'min': 'MIN',
            'number_format': 'NUMBER_FORMAT',
            'trim': 'TRIM',
            'substr': 'SUBSTR',
            'wordwrap': 'WORDWRAP',
            'sort': 'SORT',
            'count': 'COUNT',
            'next': 'NEXT',
            'object': 'OBJECT'}


tokens = ["MENOS", "MAS", "PRODUCTO", "DIVISION", "MODULO", "NUMEROS", "FLOAT", "LCORC", "RCORC", "FLAG", "LPAREN", "RPAREN", "IGUAL_IGUAL", "IDENTICO", "DISTINTO",
           "MENORQUE","MAYORQUE", "MENOROIGUAL", "MAYOROIGUAL", "ANDAND", "OROR", "NO", "PUNTOCOMA",
          "VARIABLE", "CADENASIMPLE", "CADENADOBLE","POSTDECREMENTO", "PREINCREMENTO","POSTINCREMENTO", "PREDECREMENTO", "R_LLAVE", "L_LLAVE", "COMA",
          "IGUAL", "PUNTO", "EXPONENCIACION"] + list (reserved.values())

t_MENOS = r'-';t_MAS = r'\+';t_PRODUCTO = r'\*';t_DIVISION=r'/';t_MODULO=r'%';t_COMA = r','; t_EXPONENCIACION = r'\*\*';
t_NUMEROS = r'[0-9]+';t_FLOAT = r'[0-9]+\.[0-9]+' ;t_LCORC = r'\['; t_RCORC = r'\]';t_LPAREN = r'\(';t_RPAREN = r'\)';t_R_LLAVE = r"}";t_L_LLAVE= r'{';t_IGUAL = r"="
t_FLAG = r'[SORT_REGULAR | SORT_NUMERIC | SORT_STRING | SORT_LOCALE_STRING | SORT_NATURAL | SORT_FLAG_CASE ]';
t_IGUAL_IGUAL = r'==';t_IDENTICO=r'===';t_DISTINTO=r'!=|<>'
t_MENORQUE=r'<';t_MAYORQUE=r'>';t_MENOROIGUAL=r'<=';t_MAYOROIGUAL=r'>='
t_ANDAND=r' \&\&';t_OROR=r' \|\|';t_NO=r'!'
t_PUNTOCOMA=r';';t_VARIABLE=r'\$\w+'; t_OBJECT = r'object'
t_PREINCREMENTO=r'\+\+\$\w+';t_POSTINCREMENTO=r'\$\w+\+\+';t_PREDECREMENTO=r'--\$\w+'; t_POSTDECREMENTO=r'\$\w+--'
t_IF = r'if';t_FOR = r'for';t_WHILE = r'while';t_ELSE = r'else'
t_ECHO=r'echo';
t_PRINT=r'print'
t_CADENASIMPLE = r'\'[\w\s\~\!\@\#\$\%\^\&\*\(\)\_\+\{\}\|\:\<\>\?\/\-\+\.\`\=-\[\]\"\;\,\\]*\''
t_CADENADOBLE = r'\"[\w\s\~\!\@\#\$\%\^\&\*\(\)\_\+\{\}\|\:\<\>\?\/\-\+\.\`\=-\[\]\'\;\,\\]*\"'
t_PUNTO=r'\.'
t_ignore = ' \t'
t_OR= r'or';t_AND= r'and';
t_ELSE= r'else'
t_ARRAY= r'array' ; t_LIST = r'list'
t_ELSEIF = r'elseif'
t_XOR = r'xor'
t_BOOLEAN = r'True|False';
t_FOPEN = r'fopen';
t_FPASSTHRU = r'fpassthru';
t_FEOF = r'feof';
t_FGETS = r'fgets'
t_NL2BR = r'nl2br';
t_ROUND = r'round';
t_FLOOR = r'floor';
t_CEIL = r'ceil';
t_POTENCIA = r'pow';
t_MAX =r'max';
t_MIN =r'min';
t_NUMBER_FORMAT = r'number_format';
t_TRIM = r'trim';
t_SUBSTR = r'substr';
t_WORDWRAP = r'wordwrap';
t_SORT = r'sort'
t_COUNT = r'count';
t_NEXT = r'next'

def t_error(t):
    print ("No definido'%s'" % t.value[0])
    t.lexer.skip (1)


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len (t.value)

#EJEMPLOS JOSELYN HOLGUIN
cadena = "++$hola $var 4+5"
analizadorJ = lex.lex()
analizadorJ.input(cadena)

cadena1 = "--$var $pol ($a>2) && ($b<3) 2*4 "
analizadorJ = lex.lex()
analizadorJ.input(cadena1)

cadena2 = "($a>2) || ($b<3) 6%2 $r1==$r2 $a1===$a1 && $s ! $s1"
analizadorJ = lex.lex()
analizadorJ.input(cadena2)

while True:
    tokenRec = analizadorJ.token()
    if tokenRec != None:
        print (tokenRec)
    else:
        break

#EJEMPLOS KEVIN  BRIONES
cadena3 = "if($var1 == $var2 and === 1)"
analizadorK = lex.lex()
analizadorK.input(cadena3)

cadena4 = "foreach (array(1, 2, 3, 4) as $valor) {$valor * 2;}"
analizadorK = lex.lex()
analizadorK.input(cadena4)

cadena5 = "{ $aMemberVar = \'aMemberVar Member Variable\'; $aFuncName = \'aMemberFunc\';"
analizadorK = lex.lex()
analizadorK.input(cadena5)


while True:
    tokenRed = analizadorK.token()
    if tokenRed != None:
        print (tokenRed)
    else:
        break

#EJEMPLOS DAVID LEON
cadena7 = "$VAR = \'soy una variable\'"
analizadorD = lex.lex()
analizadorD.input(cadena7)

cadena8 = "trim($cadena) count($frutitas) "
analizadorD = lex.lex()
analizadorD.input(cadena8)

cadena9 = "next($dulces) $archivo = ds ds  fopen(\"archivo.txt\", \"r\");"
analizadorD = lex.lex()
analizadorD.input(cadena9)

while True:
    tokenPru = analizadorD.token()

    if tokenPru != None:
        print (tokenPru)
    else:
        break
