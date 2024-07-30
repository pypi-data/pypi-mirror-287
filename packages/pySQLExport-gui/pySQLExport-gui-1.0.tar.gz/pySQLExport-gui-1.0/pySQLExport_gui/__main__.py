"""
================================================================================
   Project: pySQLExport-gui
   Description: A PyQt6 GUI application for managing and exporting SQL query results.
   Author: Aaron
   Email: aaron.mathis@gmail.com
   License: GNU General Public License v3.0 (GPL-3.0)
   License URL: https://www.gnu.org/licenses/gpl-3.0.en.html
================================================================================

   This file is part of pySQLExport-gui.

   pySQLExport-gui is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   pySQLExport-gui is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with pySQLExport-gui. If not, see <https://www.gnu.org/licenses/>.

================================================================================
"""


from pySQLExport_gui.new_connection_window import NewConnectionWindow
from PyQt6.QtWidgets import QApplication
import sys #Module for getting args




def main():

    app = QApplication(sys.argv)
    win = NewConnectionWindow()

    win.show()
    sys.exit(app.exec())

if __name__== '__main__':
    main()
