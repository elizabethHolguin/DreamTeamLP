import sys
import ply.yacc as sintaxis
import ply.lex as lex
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPlainTextEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget
from practica import *
from sintactic import *

#Creando instancia de QApplication
app = QApplication(sys.argv)
#Creando instancia de intergaz QApplication
window = QWidget()
window.setWindowTitle('ANALIZADOR LÉXICO Y SINTÁCTICO PHP')
window.setGeometry(70, 80, 820, 400)
window.move(60, 15)
#Colocar botones
btnvalidarlex = QPushButton()
btnvalidarlex.setText('Validar Lexico')
btnvalidarlex.setStyleSheet('QPushButton {background-color: #A3C1DA}')

btnvalidarsin = QPushButton()
btnvalidarsin.setText('Validar Sintactico')
btnvalidarsin.setStyleSheet('QPushButton {background-color: #A3C1DA}')

btnlimpiar = QPushButton()
btnlimpiar.setText('Limpiar')
btnlimpiar.setStyleSheet('QPushButton {background-color: #A3C1DA}')
#Labels
lblFuente = QLabel()
lblFuente.setText("PROPORCIONE SU CÓDIGO FUENTE EN ESTE APARTADO:")

cod = QPlainTextEdit(parent=window)
texto = cod.sizePolicy()
texto.setHorizontalPolicy(QSizePolicy.Expanding)
cod.setSizePolicy(texto)

lblAnalizador = QLabel()
lblAnalizador.setText("VERIFIQUE SU ANALIZADOR")


lblLexico = QLabel()
lblLexico.setText("LÉXICO: ")
lexico = QPlainTextEdit()
lexic = lexico.sizePolicy()
lexic.setHorizontalPolicy(QSizePolicy.Expanding)
lexico.setSizePolicy(lexic)

lblSintactico = QLabel()
lblSintactico.setText("SINTÁCTICO: ")
sintactico = QPlainTextEdit()
sintac = sintactico.sizePolicy()
sintac.setHorizontalPolicy(QSizePolicy.Expanding)
sintactico.setSizePolicy(sintac)


layoutContenedor = QHBoxLayout()
layoutCodFuente = QVBoxLayout()
layoutPrincipal = QHBoxLayout()
layoutPrinSec = QHBoxLayout()
layoutPrinTer = QHBoxLayout()

layoutButtons = QVBoxLayout()

layoutButtons.addWidget(btnvalidarlex)
layoutButtons.addWidget(btnvalidarsin)
layoutButtons.addWidget(btnlimpiar)

layoutCodFuente.addWidget(lblFuente)
layoutCodFuente.addWidget(cod)
layoutPrincipal.addLayout(layoutCodFuente)
layoutPrincipal.addLayout(layoutButtons)

layoutAnalisis = QVBoxLayout()
layoutLexSin = QVBoxLayout()
layoutLexico = QVBoxLayout()
layoutSintactico = QVBoxLayout()


layoutLexico.addWidget(lblLexico)
layoutLexico.addWidget(lexico)
layoutSintactico.addWidget(lblSintactico)
layoutSintactico.addWidget(sintactico)

layoutLexSin.addLayout(layoutLexico)
layoutLexSin.addLayout(layoutSintactico)
layoutAnalisis.addWidget(lblAnalizador)
layoutAnalisis.addLayout(layoutLexSin)


layoutContenedor.addLayout(layoutPrincipal)
layoutContenedor.addLayout(layoutAnalisis)
window.setLayout(layoutContenedor)
window.setStyleSheet ("background-color: white;")


def limpiar():
    cod.clear()
    lexico.clear()
    sintactico.clear()
btnlimpiar.clicked.connect(limpiar)




def analisisLex():
    tex = cod.toPlainText()
    lexico.clear()
    sintactico.clear()
    analizadorLexico = lex.lex()
    analizadorLexico.input(tex)


    while True:
        tokenRec = analizadorLexico.token()
        if tokenRec != None:
            lexico.appendPlainText(str(tokenRec))
            print(tokenRec)

        else:
            break

    #lexSintactico=lex.sintactic(tex)
    #sintactic.appendPlaintText(lexSintactico)

btnvalidarlex.clicked.connect(analisisLex)


def analisisSin():
    tex = cod.toPlainText()
    sintactico.clear()
    parser = sintaxis.yacc()
    result = parser.parse(tex)
    sintactico.appendPlainText(str(result))
    print(result)

btnvalidarsin.clicked.connect(analisisSin)



#Mostrando interfaz
window.show()
#Ejecutar la app desde consola
sys.exit(app.exec_())

