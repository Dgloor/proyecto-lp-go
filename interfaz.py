import sys
from PyQt5.QtWidgets import QMainWindow, QToolBar, QAction, QLabel, QPlainTextEdit, QHBoxLayout
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QMessageBox, QApplication
from PyQt5.QtGui import QFont
from lexico import *
from sintactico import parser
import re


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # Características
        self.font_size = 12

        # Acciones
        toolbar_herramientas = QToolBar()
        self.addToolBar(toolbar_herramientas)

        action_lexico = QAction("Análisis Léxico", self)
        action_lexico.triggered.connect(self.analisis_lexico)
        toolbar_herramientas.addAction(action_lexico)

        action_sintactico = QAction("Análisis Sintácico", self)
        action_sintactico.triggered.connect(self.analisis_sintactico)
        toolbar_herramientas.addAction(action_sintactico)

        action_semantico = QAction("Análisis Semántico", self)
        action_semantico.triggered.connect(self.analisis_semantico)
        toolbar_herramientas.addAction(action_semantico)

        toolbar_herramientas.addSeparator()

        action_limpiar = QAction("Limpiar todo", self)
        action_limpiar.triggered.connect(self.limpiar_todo)
        toolbar_herramientas.addAction(action_limpiar)

        # Editor de código
        self.label_input = QLabel("Editor")
        self.label_input.setFont(QFont('Arial', 10))
        self.input = QPlainTextEdit()
        self.input.setFont(QFont('Consolas', 11))

        # Salida análisis
        self.label_output = QLabel("Salida Análisis")
        self.label_output.setFont(QFont('Arial', 10))
        self.output = QPlainTextEdit()
        self.output.setReadOnly(True)
        self.output.setFont(QFont('Consolas', 11))

        # Contenedor principal
        self.layout = QHBoxLayout()
        grid = QVBoxLayout()

        grid.addWidget(self.label_input)
        grid.addWidget(self.input)

        grid.addWidget(self.label_output)
        grid.addWidget(self.output)

        self.layout.addLayout(grid)
        self.contenedor = QWidget()
        self.setCentralWidget(self.contenedor)
        self.contenedor.setLayout(self.layout)

    def analisis_lexico(self):
        try:
            codigo = self.input.toPlainText()
            self.check_empty(codigo)

            lexer.input(codigo)
            resultado = ""
            while True:
                tok = lexer.token()
                if not tok:
                    break
                resultado += f'Token: {tok.type}= "{tok.value}", Línea: {tok.lineno}, Col: {tok.lexpos}  \n'

            self.output.setPlainText(resultado)
        except Exception as e:
            self.show_error(str(e))

    def analisis_sintactico(self):
        try:
            codigo = self.input.toPlainText()
            self.check_empty(codigo)

            parser.parse(codigo)
            resultado = "No se presentaron errores durante el análisis sintáctico."
            self.output.setPlainText(resultado)
        except Exception as e:
            self.show_error(str(e))

    def analisis_semantico(self):
        try:
            codigo = self.input.toPlainText()
            self.check_empty(codigo)

            resultado = ""
            self.output.setPlainText(resultado)
        except Exception as e:
            self.show_error(str(e))

    def check_empty(self, codigo):
        if not re.match(r"(\n|\t|\s)*[^\n\t\s]+", codigo):
            raise AnalyzerException("ERROR: La entrada está vacía.")

    def limpiar_salida(self):
        self.output.setPlainText("")

    def limpiar_todo(self):
        self.input.setPlainText("")
        self.output.setPlainText("")

    def show_error(self, message):
        dlg = QMessageBox(self)
        dlg.setText(message)
        dlg.setIcon(QMessageBox.Critical)
        dlg.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName("Analizador de código GO")
    w = Window()
    w.showMaximized()
    sys.exit(app.exec_())
    # app.exec_()
