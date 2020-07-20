import sys
import practica as lexico
import sintactic as sintaxis

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
window.setWindowTitle('Analizador Léxico y Sintáctico PHP')
window.setGeometry(300, 90, 1120, 900)
window.move(60, 15)


#Mostrando interfaz
window.show()
#Ejecutar la app desde consola
sys.exit(app.exec_())

