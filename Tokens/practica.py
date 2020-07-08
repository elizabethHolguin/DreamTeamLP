#JOSELYN HOLGUIN
import ply.lex as lex

reserved={
    'if' : 'IF',
    'elif' : 'ELIF',
    'else' : 'ELSE',
    'while' : 'WHILE',
    'for' : 'FOR',
    'echo' : 'ECHO'}

tokens=("MENOS","MAS","PRODUCTO","DIVISION","NUMEROS","LPAREN","RPAREN","IGUAL","ID","POTENCIA","COMPARA")+tuple(reserved.values())

t_MENOS=r'-'
t_MAS=r'\+'
t_PRODUCTO=r'\*'
t_NUMEROS=r'[0-9]+'
t_LPAREN= r'\('
t_RPAREN= r'\)'
t_IGUAL=r'='
#t_ID=r'[a-z][a-zA-Z0-9_]*'
t_POTENCIA=r'\*\*'
t_COMPARA=r'[!<>=]='
t_IF=r'if'
t_ECHO=r'echo'
t_FOR=r'for'
t_WHILE=r'while'
t_ELIF=r'elif'

t_ignore=' \t'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_error(t):
    print("No se ha reconocido'%s'"%t.value[0])
    t.lexer.skip(1)

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

cadena="for + if mds "

analizadorL= lex.lex()
analizadorL.input(cadena)

while True:
    tokenRec = analizadorL.token()
    if tokenRec!=None:
        print(tokenRec)
    else:
        break
