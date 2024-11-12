import sys # Importamos el módulo sys para poder utilizar sys.exit() para salir de la aplicación
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox 
from Interfaz import Ui_MainWindow  

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        
        self.ui.pushButton.clicked.connect(self.verificar_campos) # Conectamos el evento clicked de un botón con una función
        self.ui.pushButton_2.clicked.connect(self.vaciar_campos) # Conectamos el evento clicked de un botón con una función
        
    def verificar_campos(self):
        if self.ui.lineEdit.text() == "" or self.ui.lineEdit_2.text() == "" or self.ui.lineEdit_3.text() == "" or self.ui.lineEdit_4.text() == "" or self.ui.lineEdit_5.text() == "":
                mensaje = QMessageBox()
                mensaje.setWindowTitle("Error")
                mensaje.setIcon(QMessageBox.Critical)
                mensaje.setText("Error al insertar propietario")
                mensaje.width = 200
                mensaje.height = 200
                mensaje.exec_()
        else:
            mensaje = QMessageBox()
            mensaje.setWindowTitle("Correcto")
            mensaje.setIcon(QMessageBox.Information)
            mensaje.setText("Propietario insertado correctamente")
            mensaje.exec_()
    
    def vaciar_campos(self):
        self.ui.lineEdit_6.setText("")
        self.ui.lineEdit_7.setText("")
    
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mi_app = VentanaPrincipal()
    mi_app.show()
    sys.exit(app.exec_())
    
    
    

