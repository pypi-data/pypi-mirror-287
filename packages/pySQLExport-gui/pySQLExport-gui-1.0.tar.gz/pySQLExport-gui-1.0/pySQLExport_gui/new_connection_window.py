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



from PyQt6.QtGui import ( 
    QFont, QFontDatabase, QAction, 
    QKeySequence, QStandardItemModel, QStandardItem

)

from PyQt6.QtCore import (
    QMetaObject, Qt, QCoreApplication, 
    QRect
)

from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, 
    QLineEdit, QPushButton, QFormLayout, 
    QVBoxLayout, QLabel, QFrame,
    QHBoxLayout, QSizePolicy,
    QMessageBox, QFileDialog, QAbstractItemView,
    QComboBox, QMenu, QCheckBox, 
    QTextEdit,QTabWidget, QTableView,
    QMenuBar, QStatusBar, QHeaderView
)



from pySQLExport_gui.pySQLExport import PySQLExport

class NewConnectionWindow(QMainWindow):
    def __init__(self):
        self.main_app = PySQLExport()
        super(NewConnectionWindow, self).__init__()
       
        # Set window geometry and title   
        self.setGeometry(200, 200, 400, 200)  
        self.setWindowTitle("pySQLExport")

        self.init_ui()

    def init_ui(self):
        self.central_widget = QWidget()  # Create a central widget
        self.setCentralWidget(self.central_widget)  # Set the central widget

        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(40, 20, 40, 20)  # Set margins (left, top, right, bottom)
        self.central_widget.setLayout(self.main_layout)

        self.render_header()
        self.main_layout.addSpacing(20)
        self.render_HLine()
        self.main_layout.addSpacing(20)
        self.render_info_text()
        self.main_layout.addSpacing(40)

        self.render_form() # Render form layout
        self.set_window_style() 

    def render_HLine(self):
        # Add a horizontal line separator
        line = QFrame()
        line.setFrameShape(QFrame.Shape.HLine)
        line.setFrameShadow(QFrame.Shadow.Sunken)
        self.main_layout.addWidget(line)

    def render_header(self):
      # Create and add header text
        self.header_label = QLabel("pySQLExport")
        self.header_font = QFontDatabase.systemFont(QFontDatabase.SystemFont.TitleFont)
        self.header_font.setPointSize(48)  # Ensure the font size is set
        self.header_font.setBold(True)  # Ensure the font weight is set to bold
        self.header_label.setFont(self.header_font)
        self.header_label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Center the text
        self.main_layout.addWidget(self.header_label)

        self.version_label = QLabel(self.main_app.version)
        self.version_font = QFontDatabase.systemFont(QFontDatabase.SystemFont.SmallestReadableFont)
        self.version_font.setPointSize(14)  # Ensure the font size is set
        self.version_label.setFont(self.version_font)
        self.version_label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Center the text        
        self.main_layout.addWidget(self.version_label)

    def render_info_text(self):
        # Add informative text
        self.info_label = QLabel("Please enter database server details in order to connect to a database.")
        self.info_font = QFontDatabase.systemFont(QFontDatabase.SystemFont.GeneralFont)
        self.info_font.setPointSize(12)  # Ensure the font size is set
        self.info_label.setFont(self.info_font)
        self.info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Center the text
        self.info_label.setContentsMargins(0, 20, 0, 0)        
        self.main_layout.addWidget(self.info_label)

    def render_form(self):
        self.form_layout = QFormLayout()
        self.form_layout.setContentsMargins(0, 0, 0, 0)  # Set margins (left, top, right, bottom)
        self.form_layout.setSpacing(10)  # Set spacing between form elements
        self.central_widget.setLayout(self.form_layout)  # Set the layout on the central widget

        # Create and add form elements
        self.server_input = QLineEdit()
        self.username_input = QLineEdit()
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.database_input = QLineEdit()
        
        self.port_input = QLineEdit()
        self.port_input.setText("3306")
        self.port_input.setMaxLength(5)  # Limit input to 8 characters
        self.port_input.setFixedWidth(50)  # Set a fixed width appropriate for 5 characters
        
        # Add a dropdown for selecting database type
        self.db_type_input = QComboBox()
        self.db_type_input.addItems(["MySQL", "PostgreSQL"])
        self.db_type_input.currentIndexChanged.connect(self.update_port)  # Connect the signal to update port

        
        self.form_layout.addRow("Database Type:", self.db_type_input)
        self.form_layout.addRow("Server:", self.server_input)
        self.form_layout.addRow("Username:", self.username_input)
        self.form_layout.addRow("Password:", self.password_input)
        self.form_layout.addRow("Database:", self.database_input)
        self.form_layout.addRow("Port:", self.port_input)

        #Add form to main layout
        self.main_layout.addLayout(self.form_layout)

        # Create and add a submit button
        # Create and configure the establish connection button
        self.submit_button = QPushButton("Establish Connection")
        self.submit_button.clicked.connect(self.handle_connect) # Connect to function when pressed
        self.submit_button.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        # Create a horizontal layout to center the button
        self.button_layout = QHBoxLayout()
        self.button_layout.addStretch()
        self.button_layout.addWidget(self.submit_button)
        self.main_layout.addLayout(self.button_layout)        
        # Apply styles
         
    def update_port(self):
        if self.db_type_input.currentText() == "PostgreSQL":
            self.port_input.setText("5432")
        else:
            self.port_input.setText("3306")

    def set_window_style(self):
        self.setStyleSheet("""
            QComboBox { padding: 5px; border: 1px solid #ccc }
            QLineEdit { padding: 5px;border: 1px solid #ccc;border-radius: 5px;}
            QPushButton {  padding: 5px 10px;background-color: #007bff;color: white;border: none;border-radius: 5px;}
            QPushButton:hover {background-color: #0056b3;}
            QLabel#errorLabel { color: red; }
            QHeaderView::section {
                background-color: #d3d3d3;  /* Gray background for headers */
            }
            QTableView {
                gridline-color: #d3d3d3;  /* Gray grid lines */
            }
            QTableView::item {
                border-left: 1px solid #d3d3d3;  /* Left border of each cell */
                border-right: 1px solid #d3d3d3; /* Right border of each cell */
            }                           
        """)     
    def render_error_text(self, message):

        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Critical)
        msg_box.setWindowTitle("pySQLExport - Error")
        msg_box.setText(message)
        msg_box.exec()            

    def handle_connect(self):
        db_type = self.db_type_input.currentText()
        username = self.username_input.text()
        password = self.password_input.text()
        database = self.database_input.text()
        port = self.port_input.text()
        server = self.server_input.text()

        if self.main_app.connect_db(db_type, server, username, password, database, port):
            # Assuming the login is successful
            from pySQLExport_gui.main_window import MainWindow 
            self.main_window = MainWindow(self.main_app)
            self.main_window.show()
            self.close()
        else:
            self.render_error_text(f"Could not connect: {self.main_app.error}")
