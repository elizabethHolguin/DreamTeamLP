import sys
#import practica as lexico
#import sintactic as sintactico
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QErrorMessage
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPlainTextEdit
from PyQt5.QtWidgets import QSizePolicy

#Creando instancia de QApplication
app = QApplication(sys.argv)
#Creando instancia de intergaz QApplication
window = QWidget()
window.setWindowTitle('ANALIZADOR LÉXICO Y SINTÁCTICO PHP')
window.setGeometry(70, 80, 820, 400)
window.move(60, 15)
#Colocar botones
btnvalidar = QPushButton()
btnvalidar.setText('Validar')
btnvalidar.setStyleSheet('QPushButton {background-color: #A3C1DA}')

btnlimpiar = QPushButton()
btnlimpiar.setText('Limpiar')
btnlimpiar.setStyleSheet('QPushButton {background-color: #A3C1DA}')
#Labels
lblFuente = QLabel()
lblFuente.setText("PROPORCIONE SU CÓDIGO FUENTE EN ESTE APARTADO:")

cod = QPlainTextEdit()
texto = cod.sizePolicy()
texto.setHorizontalPolicy(QSizePolicy.Expanding)
cod.setSizePolicy(texto)

lblAnalizador = QLabel()
lblAnalizador.setText("VERIFIQUE SU ANALIZADOR")
lblAnalizador.setAlignment(Qt.AlignLeft)

lblLexico = QLabel()
lblLexico.setText("LÉXICO: ")
lexico = QPlainTextEdit()
lex = lexico.sizePolicy()
lex.setHorizontalPolicy(QSizePolicy.Expanding)
lexico.setSizePolicy(lex)

lblSintactico = QLabel()
lblSintactico.setText("SINTÁCTICO: ")
sintactico = QPlainTextEdit()
sintac = sintactico.sizePolicy()
sintac.setHorizontalPolicy(QSizePolicy.Expanding)
sintactico.setSizePolicy(sintac)

lblErrorSintac = QLabel()
lblErrorSintac.setText("ERRORES: ")
errorSintac = QPlainTextEdit()
errSintax = errorSintac.sizePolicy()
errSintax.setHorizontalPolicy(QSizePolicy.Expanding)
errorSintac.setSizePolicy(errSintax)

layoutContenedor = QHBoxLayout()
layoutCodFuente = QVBoxLayout()
layoutPrincipal = QHBoxLayout()
layoutPrinSec = QHBoxLayout()
layoutPrinTer = QHBoxLayout()

layoutButtons = QVBoxLayout()

layoutButtons.addWidget(btnvalidar)
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
#layoutSint.addWidget(lblSintErr)
#layoutSint.addWidget(errorSint)
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


#Mostrando interfaz
window.show()
#Ejecutar la app desde consola
sys.exit(app.exec_())

