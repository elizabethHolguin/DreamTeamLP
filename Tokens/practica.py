import ply.lex as lex

reserved = {'or': 'OR',
            'and': 'AND',
            'if': 'IF',
            'else': 'ELSE',
            'while': 'WHILE',
            'break': 'BREAK',
            'for': 'FOR',
            'echo': 'ECHO',
            'print':'PRINT',
            'abstract': 'ABSTRACT',
            'array': 'ARRAY',
            'as': 'AS',
            'case': 'CASE',
            'catch': 'CATCH',
            'const': 'CONST',
            'continue': 'CONTINUE',
            'declare': 'DECLARE',
            'default': 'DEFAULT',
            'do': 'DO',
            'elseif': 'ELSEIF',
            'empty': 'EMPTY',
            'enddeclare': 'ENDDECLARE',
            'endfor': 'ENDFOR',
            'endforeach': 'ENDFOREACH',
            'endif': 'ENDIF',
            'endswitch': 'ENDSWITCH',
            'endwhile': 'ENDWHILE',
            'exit': 'EXIT',
            'extends': 'EXTENDS',
            'final': 'FINAL',
            'foreach': 'FOREACH',
            'function': 'FUNCTION',
            'global': 'GLOBAL',
            'goto': 'GOTO',
            'implements': 'IMPLEMENTS',
            'include': 'INCLUDE',
            'include_once': 'INCLUDE_ONCE',
            'instanceof': 'INSTANCEOF',
            'interface': 'INTERFACE',
            'isset': 'ISSET',
            'list': 'LIST',
            'new': 'NEW',
            'private': 'PRIVATE',
            'protected': 'PROTECTED',
            'public': 'PUBLIC',
            'require': 'REQUIRE',
            'require_once': 'REQUIRE_ONCE',
            'return': 'RETURN',
            'static': 'STATIC',
            'switch': 'SWITCH',
            'throw': 'THROW',
            'try': 'TRY',
            'unset': 'UNSET',
            'use': 'USE',
            'var': 'VAR',
            'xor': 'XOR',
            'callable': 'CALLABLE',
            'clone': 'CLONE',
            'die': 'DIE',
            'eval': 'EVAL',
            'insteadof': 'INSTEADOF',
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
            'maxmix': 'MAXMIN',
            'number_format': 'NUMBER_FORMAT',
            'trim': 'TRIM',
            'substr': 'SUBSTR',
            'wordwrap': 'WORDWRAP',
            'sort': 'SORT',
            'count': 'COUNT',
            'next': 'NEXT',
            'getclass': 'GETCLASS',
            'is_a': 'IS_A'}

constants = {'class': 'CLASS', 'dir': 'DIR', 'file': 'FILE', 'line': 'LINE', 'method': 'METHOD',
             'namespace': 'NAMESPACE', 'trait': 'TRAIT'}

tokens = ["MENOS", "MAS", "PRODUCTO", "DIVISION", "MODULO", "NUMEROS", "LPAREN", "RPAREN", "IGUAL_IGUAL", "IDENTICO", "DISTINTO",
          "NOIDENTICO", "MENORQUE","MAYORQUE", "MENOROIGUAL", "MAYOROIGUAL", "ANDAND", "OROR", "NO", "ID", "PUNTOCOMA",
          "VARIABLE", "CADENASIMPLE", "CADENADOBLE", "PREINCREMENTO","POSTINCREMENTO", "PREDECREMENTO", "R_LLAVE", "L_LLAVE", "COMA",
          "IGUAL", "APOSTROFE", "PUNTO"] + list (reserved.values ()) + list (constants.values())

t_MENOS = r'-';t_MAS = r'\+';t_PRODUCTO = r'\*';t_DIVISION=r'/';t_MODULO=r'%';t_COMA = r','
t_NUMEROS = r'[0-9]+';t_LPAREN = r'\(';t_RPAREN = r'\)';t_R_LLAVE = r"}";t_L_LLAVE= r'{';t_IGUAL = r"="
t_IGUAL_IGUAL = r'==';t_IDENTICO=r'===';t_DISTINTO=r'!=|<>';t_NOIDENTICO=r'!=='
t_MENORQUE=r'<';t_MAYORQUE=r'>';t_MENOROIGUAL=r'<=';t_MAYOROIGUAL=r'>='
t_ANDAND=r' \&\&';t_OROR=r' \|\|';t_NO=r'!'
t_PUNTOCOMA=r';';t_VARIABLE=r'\$\w+'
t_PREINCREMENTO=r'\+\+\$\w+';t_POSTINCREMENTO=r'\$\w+\+\+';t_PREDECREMENTO=r'--\$\w+'
t_IF = r'if';t_FOR = r'for';t_WHILE = r'while';t_ELSE = r'else'
t_ECHO=r'echo';t_PRINT=r'print'
t_BREAK=r'break'
t_CADENASIMPLE = r'((\')[a-zA-Z_][a-zA-Z_0-9]*(\'))'
t_CADENADOBLE = r'((\")[a-zA-Z_][a-zA-Z_0-9]*(\"))'
t_PUNTO=r'\.'
t_APOSTROFE=r'\'|\"'
t_ignore = ' \t'
t_CLASS = r'class';t_DIR=r'dir';t_FILE=r'file';t_FUNCTION=r'function';t_LINE=r'line';t_METHOD=r'method';t_NAMESPACE=r'namespace'
t_TRAIT=r'trait'
t_OR= r'or';t_AND= r'and';t_ELSE= r'else'
t_ABSTRACT= r'abstract';t_ARRAY= r'array';t_AS= r'as';t_CASE = r'case';t_CATCH = r'catch'
t_CONST = r'const'; t_CONTINUE = r'continue'; t_DECLARE= r'declare'; t_DEFAULT = r'default'; t_DO= r'do'
t_ELSEIF = r'elseif'; t_EMPTY =r'empty'; t_ENDDECLARE= r'enddeclare'; t_ENDFOR =  r'endfor'; t_ENDFOREACH= r'endforeach'
t_ENDIF = r'endif'; t_ENDSWITCH = r'endswitch'; t_ENDWHILE= r'endwhile'; t_EXIT = 'exit'; t_EXTENDS = r'extends'
t_FINAL = r'final'; t_FOREACH = r'foreach'; t_GLOBAL = r'global'; t_GOTO = r'goto'
t_IMPLEMENTS = r'implements'; t_INCLUDE = r'include'; t_INCLUDE_ONCE = r'include_once'; t_INSTANCEOF = r'instanceof'
t_INTERFACE = r'interface'; t_ISSET = r'isset'; t_LIST = r'list'; t_NEW = r'new'; t_PRIVATE = r'private'
t_PROTECTED = r'protected'; t_PUBLIC = r'public'; t_REQUIRE = r'require'; t_REQUIRE_ONCE = r'require_once'
t_RETURN = r'return'; t_STATIC = r'static'; t_SWITCH = r'switch'; t_THROW= r'throw'; t_TRY = r'try'; t_UNSET = r'unset'
t_USE = r'use'; t_VAR = r'var'; t_XOR = r'xor'; t_CALLABLE = r'callable'; t_CLONE = r'clone'; t_DIE = r'die'
t_EVAL = r'eval'; t_INSTEADOF = r'insteadof'
t_BOOLEAN = r'True|False'; t_FOPEN = r'fopen'; t_FPASSTHRU = r'fpassthru'; t_FEOF = r'feof';t_FGETS = r'fgets'
t_NL2BR = r'nl2br'; t_ROUND = r'round'; t_FLOOR = r'floor'; t_CEIL = r'ceil'; t_POTENCIA = r'pow'; t_MAXMIN ='maxmin'
t_NUMBER_FORMAT = r'number_format'; t_TRIM = r'trim'; t_SUBSTR = r'substr'; t_WORDWRAP = r'wordwrap'; t_SORT = r'sort'
t_COUNT = r'count'; t_NEXT = r'next'; t_GETCLASS = r'getclass'; t_IS_A = r'is_a'

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

#EJEMPLOS JOSELYN HOLGUIN
cadena = "++$hola $var hello 4+5"
analizadorJ = lex.lex()
analizadorJ.input(cadena)

cadena1 = "--$var $pol ($a>2) && ($b<3) 2*4 "
analizadorJ = lex.lex()
analizadorJ.input(cadena1)

cadena2 = "($a>2) || ($b<3) 6%2 $r1==$r2 $a1===$a1 hola && hola $s ! $s1"
analizadorJ = lex.lex()
analizadorJ.input(cadena2)

while True:
    tokenRec = analizadorJ.token()
    if tokenRec != None:
        print (tokenRec)
    else:
        break

#EJEMPLOS KEVIN  BRIONES
cadena3 = "if($var1 == $var2 and var === 1)"
analizadorK = lex.lex()
analizadorK.input(cadena3)

cadena4 = "foreach (array(1, 2, 3, 4) as $valor) {$valor * 2;}"
analizadorK = lex.lex()
analizadorK.input(cadena4)

cadena5 = "class Foo { public $aMemberVar = \'aMemberVar Member Variable\'; public $aFuncName = \'aMemberFunc\';"
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

cadena9 = "next($dulces) $archivo = fopen(\"archivo.txt\", \"r\");"
analizadorD = lex.lex()
analizadorD.input(cadena9)

while True:
    tokenPru = analizadorD.token()
    if tokenPru != None:
        print (tokenPru)
    else:
        break
