from pySQLExport_gui.gui import NewConnectionWindow, MainWindow
from PyQt6.QtWidgets import QApplication
import sys




def main():

    app = QApplication(sys.argv)
    win = NewConnectionWindow()

    win.show()
    sys.exit(app.exec())

if __name__== '__main__':
    main()
