import ply.lex as lex

reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'break': 'BREAK',
    'for': 'FOR',
    'echo': 'ECHO',
    'print':'PRINT'}

tokens = ["MENOS", "MAS", "PRODUCTO", "DIVISION", "MODULO", "NUMEROS", "LPAREN", "RPAREN", "IGUAL", "IDENTICO", "DISTINTO", "NOIDENTICO", "MENORQUE",
          "MAYORQUE", "MENOROIGUAL", "MAYOROIGUAL", "AND", "OR", "NO", "ID", "PUNTOCOMA", "VARIABLE", "CADENA", "PREINCREMENTO",
          "POSTINCREMENTO", "PREDECREMENTO"] + list (reserved.values ())

t_MENOS = r'-'
t_MAS = r'\+'
t_PRODUCTO = r'\*'
t_DIVISION=r'/'
t_MODULO=r'%'
t_NUMEROS = r'[0-9]+'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_IGUAL = r'=='
t_IDENTICO=r'==='
t_DISTINTO=r'!=|<>'
t_NOIDENTICO=r'!=='
t_MENORQUE=r'<'
t_MAYORQUE=r'>'
t_MENOROIGUAL=r'<='
t_MAYOROIGUAL=r'>='
t_AND=r' \&\&'
t_OR=r' \|\|'
t_NO=r'!'
t_PUNTOCOMA=r';'
t_VARIABLE=r'\$\w+'
t_PREINCREMENTO=r'\+\+\$\w+'
t_POSTINCREMENTO=r'\$\w+\+\+'
t_PREDECREMENTO=r'--\$\w+'
t_IF = r'if'
t_FOR = r'for'
t_WHILE = r'while'
t_ELSE = r'else'
t_ECHO=r'echo'
t_PRINT=r'print'
t_BREAK=r'break'
t_CADENA = r'[a-zA-Z_][a-zA-Z_0-9]*'
t_ignore = ' \t'


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get (t.value, 'ID')
    return t


def t_error(t):
    print ("No se ha reconocido'%s'" % t.value[0])
    t.lexer.skip (1)


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len (t.value)


print("JOSELYN HOLGUIN (EJEMPLOS):")
cadena = "++$hola $var hello 4+5"
analizadorL = lex.lex()
analizadorL.input(cadena)

cadena1 = "--$var $pol ($a>2) && ($b<3) 2*4 "
analizadorL = lex.lex()
analizadorL.input(cadena1)

cadena2 = "($a>2) || ($b<3) 6%2 $r1==$r2 $a1===$a1 hola && hola $s ! $s1"
analizadorL = lex.lex()
analizadorL.input(cadena2)


while True:
    tokenRec = analizadorL.token()
    if tokenRec != None:
        print (tokenRec)
    else:
        break
