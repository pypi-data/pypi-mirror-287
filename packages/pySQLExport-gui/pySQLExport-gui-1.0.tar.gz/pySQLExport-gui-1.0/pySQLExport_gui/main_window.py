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
    QKeySequence, QStandardItemModel, QStandardItem, QMouseEvent

)

from PyQt6.QtCore import (
    QMetaObject, Qt, QCoreApplication, 
    QRect, pyqtSlot 
)

from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, 
    QLineEdit, QPushButton, QFormLayout, 
    QVBoxLayout, QLabel, QFrame,
    QHBoxLayout, QSizePolicy,
    QMessageBox, QFileDialog, QAbstractItemView,
    QComboBox, QMenu, QCheckBox, 
    QTextEdit,QTabWidget, QTableView,
    QMenuBar, QStatusBar, QHeaderView, QLayout 
)

from pySQLExport_gui.pySQLExport import PySQLExport


class MainWindow(QMainWindow):
    def __init__(self, main_app):
        super(MainWindow, self).__init__()
        self.main_app = main_app
        self.setGeometry(200, 200, 1024, 768)
        self.setWindowTitle("pySQLExport")
        self.init_ui()
        self.setCentralWidget(self.centralwidget)
        self.retranslate_ui()
        QMetaObject.connectSlotsByName(self)
        self.results = None
        self.columns = None
        self.clipboard = {"data": [], "columns": []}        

    def init_ui(self):
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)  # Add margins
        self.verticalLayout.setObjectName("verticalLayout")
       
        self.render_tab_table()
        self.render_query_form()
        self.render_menu_bar()
        self.set_window_style()

    def render_error_text(self, message):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Critical)
        msg_box.setWindowTitle("pySQLExport - Error")
        msg_box.setText(message)
        msg_box.exec()            

    def render_detailed_error_text(self, e):
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.setWindowTitle("pySQLExport - Error")
        msg.setText("An error occurred:                                            ")
        msg.setInformativeText("Please see the details below.")
        msg.setDetailedText(e)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()

    def render_info_text(self, message):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Information)
        msg_box.setWindowTitle("pySQLExport - Info")
        msg_box.setText(message)
        msg_box.exec()           
    
    def ask_user(self, title, message):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Question)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        msg_box.setDefaultButton(QMessageBox.StandardButton.No)
        
        response = msg_box.exec()

        if response == QMessageBox.StandardButton.Yes:
            return True
        else:
            return False
        
    def render_query_form(self):
        self.form_layout = QFormLayout()
        self.form_layout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.form_layout.setObjectName("form_layout")

        self.label_sql_query = QLabel(self.centralwidget)
        self.label_sql_query.setObjectName("label_sql_query")

        # Create a horizontal layout to hold the label, spacer, and text edit
        row_layout = QHBoxLayout()
        row_layout.addWidget(self.label_sql_query)

        # Add a spacer item
        spacer = QWidget(self.centralwidget)
        spacer.setFixedWidth(20)  # Adjust the width of the spacer as needed
        row_layout.addWidget(spacer)

        self.text_sql_query = QTextEdit(self.centralwidget)
        self.text_sql_query.setObjectName("text_sql_query")
        row_layout.addWidget(self.text_sql_query)

        self.form_layout.setLayout(0, QFormLayout.ItemRole.FieldRole, row_layout)
        self.verticalLayout.addLayout(self.form_layout, stretch=1)

        self.query_button = QPushButton(self.centralwidget)
        self.query_button.setObjectName("query_button")
        self.query_button.setText("Execute Query")
        self.query_button.clicked.connect(lambda: self.run_query(self.text_sql_query.toPlainText())) # Connect to function when pressed

        self.form_layout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.query_button)

        self.append_check_box = QCheckBox("Append results of query to existing dataset", self.centralwidget)
        self.append_check_box.setObjectName("append_check_box")
        self.form_layout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.append_check_box)

        self.new_tab_check_box = QCheckBox("Open results of query in a new tab", self.centralwidget)
        self.new_tab_check_box.setObjectName("new_tab_check_box")
        self.form_layout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.new_tab_check_box)
        
        self.button_layout = QHBoxLayout()
        self.button_layout.addStretch()
        self.button_layout.addWidget(self.query_button)
        self.verticalLayout.addLayout(self.button_layout)

        #self.verticalLayout.addLayout(self.formLayout_2, stretch=1)

    def render_tab_table(self):
        
        self.tab_widget = QTabWidget(self.centralwidget)  
        self.tab_widget.setObjectName("tab_widget")
        self.tab_widget.setTabsClosable(True)
        self.tab_widget.tabCloseRequested.connect(self.close_tab)
        self.tab_widget.addTab(QWidget(), "New +")
        self.tab_widget.tabBarClicked.connect(self.handle_tab_click)
        self.add_new_tab()
        self.verticalLayout.addWidget(self.tab_widget, stretch=9)  # Add the tabWidget with stretch factor


    @pyqtSlot(int)
    def handle_tab_click(self, index):
        if index == self.tab_widget.count() - 1:  # If "New +" tab is clicked
            new_tab_index = self.add_new_tab()
            self.tab_widget.setCurrentIndex(new_tab_index)

    def add_new_tab(self):
        new_tab = QWidget()
        new_tab.setObjectName(f"tab_{self.tab_widget.count() + 1}")
        new_tab_layout = QVBoxLayout(new_tab)
        new_tab_layout.setContentsMargins(0, 0, 0, 0)

        new_table_view = QTableView(new_tab)
        new_table_view.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        new_table_view.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)  # Set selection behavior to rows
        new_table_view.setObjectName(f"table_view_{self.tab_widget.count() + 1}")
        new_tab_layout.addWidget(new_table_view)

        tab_num = 1 if self.tab_widget.count() == 1 else self.tab_widget.count()

        # Insert the new tab before the "New +" tab
        index = self.tab_widget.count() - 1
        self.tab_widget.insertTab(index, new_tab, f"DataView {tab_num}")
        self.tab_widget.setCurrentWidget(new_tab)
        return index
    
    def close_tab(self, index):
        if self.tab_widget.count() != 2 and index != self.tab_widget.count() - 1:  # Prevent closing "New +" tab
            self.tab_widget.removeTab(index)

    def render_menu_bar(self):
        self.menubar = QMenuBar(self)
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)

        # FILE Menu
        self.menu_file = QMenu("File", self.menubar)
        self.menu_file.setObjectName("menu_file")

        #New Connection
        self.action_new_connection = QAction("New Connection", self)
        self.action_new_connection.setObjectName("action_new_connection")
        self.action_new_connection.setShortcut(QKeySequence('Ctrl+N'))
        self.action_new_connection.setStatusTip("Create a new connection")
        self.action_new_connection.triggered.connect(self.new_connection)
        self.menu_file.addAction(self.action_new_connection)

        #Copy
        self.action_copy = QAction("Copy", self)
        self.action_copy.setObjectName("action_copy")
        self.action_copy.setShortcut(QKeySequence('Ctrl+C'))
        self.action_copy.setStatusTip("Copy selected rows")
        self.action_copy.triggered.connect(self.copy_selected)
        self.menu_file.addAction(self.action_copy)

        #Paste
        self.action_paste = QAction("Paste", self)
        self.action_paste.setObjectName("action_paste")
        self.action_paste.setShortcut(QKeySequence('Ctrl+V'))
        self.action_paste.setStatusTip("Paste selection into current table")
        self.action_paste.triggered.connect(self.paste_selected)
        self.menu_file.addAction(self.action_paste)

        #Exit
        self.action_exit = QAction("Exit", self)
        self.action_exit.setObjectName("action_exit")
        self.action_exit.setShortcut(QKeySequence('Ctrl+Q'))
        self.action_exit.setStatusTip("Close database and exit pySQLExport")        
        self.action_exit.triggered.connect(lambda: self.exit_app())
        self.menu_file.addAction(self.action_exit)        

        #Export Menu
        self.menu_export = QMenu("Export", self.menubar)
        self.menu_export.setObjectName("menu_export")
        #Export Selection
                
        # Export Selection submenu
        self.menu_export_selection = QMenu("Export Selection", self.menu_export)
        self.menu_export.addMenu(self.menu_export_selection)

        self.action_export_selection_to_csv = QAction("To CSV", self)
        self.action_export_selection_to_csv.setStatusTip("Export selected items to CSV format")
        self.action_export_selection_to_csv.triggered.connect(lambda: self.export("selection", "csv"))
        self.menu_export_selection.addAction(self.action_export_selection_to_csv)

        self.action_export_selection_to_json = QAction("To JSON", self)
        self.action_export_selection_to_json.setStatusTip("Export selected items to JSON format")
        self.action_export_selection_to_json.triggered.connect(lambda: self.export("selection", "json"))
        self.menu_export_selection.addAction(self.action_export_selection_to_json)

        self.action_export_selection_to_html = QAction("To HTML", self)
        self.action_export_selection_to_html.setStatusTip("Export selected items to HTML format")
        self.action_export_selection_to_html.triggered.connect(lambda: self.export("selection", "html"))
        self.menu_export_selection.addAction(self.action_export_selection_to_html)

        self.action_export_selection_to_xml = QAction("To XML", self)
        self.action_export_selection_to_xml.setStatusTip("Export selected items to XML format")
        self.action_export_selection_to_xml.triggered.connect(lambda: self.export("selection", "xml"))
        self.menu_export_selection.addAction(self.action_export_selection_to_xml)

        self.actionExportSelectionToExcel = QAction("To Excel", self)
        self.actionExportSelectionToExcel.setStatusTip("Export selected items to Excel format")
        self.actionExportSelectionToExcel.triggered.connect(lambda: self.export("selection", "excel"))
        self.menu_export_selection.addAction(self.actionExportSelectionToExcel)

        self.action_export_selection_to_parquet = QAction("To Parquet", self)
        self.action_export_selection_to_parquet.setStatusTip("Export selected items to Parquet format")
        self.action_export_selection_to_parquet.triggered.connect(lambda: self.export("selection", "parquet"))
        self.menu_export_selection.addAction(self.action_export_selection_to_parquet)

        self.action_export_selection_to_hdf5 = QAction("To HDF5", self)
        self.action_export_selection_to_hdf5.setStatusTip("Export selected items to HDF5 format")
        self.action_export_selection_to_hdf5.triggered.connect(lambda: self.export("selection", "hdf5"))
        self.menu_export_selection.addAction(self.action_export_selection_to_hdf5)        

        # Export All submenu
        self.menu_export_all = QMenu("Export All", self.menu_export)
        self.menu_export.addMenu(self.menu_export_all)

        self.action_export_all_to_csv = QAction("To CSV", self)
        self.action_export_all_to_csv.setStatusTip("Export all items to CSV format")
        self.action_export_all_to_csv.triggered.connect(lambda: self.export("all", "csv"))
        self.menu_export_all.addAction(self.action_export_all_to_csv)

        self.action_export_all_to_json = QAction("To JSON", self)
        self.action_export_all_to_json.setStatusTip("Export all items to JSON format")
        self.action_export_all_to_json.triggered.connect(lambda: self.export("all", "json"))
        self.menu_export_all.addAction(self.action_export_all_to_json)

        self.action_export_all_to_html = QAction("To HTML", self)
        self.action_export_all_to_html.setStatusTip("Export all items to HTML format")
        self.action_export_all_to_html.triggered.connect(lambda: self.export("all", "html"))
        self.menu_export_all.addAction(self.action_export_all_to_html)

        self.action_export_all_to_xml = QAction("To XML", self)
        self.action_export_all_to_xml.setStatusTip("Export all items to XML format")
        self.action_export_all_to_xml.triggered.connect(lambda: self.export("all", "xml"))
        self.menu_export_all.addAction(self.action_export_all_to_xml)

        self.action_export_all_to_excel = QAction("To Excel", self)
        self.action_export_all_to_excel.setStatusTip("Export all items to Excel format")
        self.action_export_all_to_excel.triggered.connect(lambda: self.export("all", "excel"))
        self.menu_export_all.addAction(self.action_export_all_to_excel)

        self.action_export_all_to_parquet = QAction("To Parquet", self)
        self.action_export_all_to_parquet.setStatusTip("Export all items to Parquet format")
        self.action_export_all_to_parquet.triggered.connect(lambda: self.export("all", "parquet"))
        self.menu_export_all.addAction(self.action_export_all_to_parquet)

        self.action_export_all_to_hdf5 = QAction("To HDF5", self)
        self.action_export_all_to_hdf5.setStatusTip("Export all items to HDF5 format")
        self.action_export_all_to_hdf5.triggered.connect(lambda: self.export("all", "hdf5"))
        self.menu_export_all.addAction(self.action_export_all_to_hdf5)
       

        #Add MenuFile/MenuExport action to menubar            
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_export.menuAction())       

        self.statusbar = QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

    def is_tableview_empty(self, table_view):
        model = table_view.model()
        if model is None:
            return True  # If there is no model, consider the table view empty
    
        return model.rowCount() == 0  

    def copy_selected(self):
        table_view = self.get_active_tableview()
        
        if self.is_tableview_empty(table_view):
            self.render_info_text("Please run a query first.")
            return

        selection_model = table_view.selectionModel()
        selected_indexes = selection_model.selectedIndexes()

        if not selected_indexes:
            self.render_info_text("Please make a valid selection.")
            return

        # Get the model associated with the QTableView
        model = table_view.model()

        # Get the selected data
        selected_data = {}
        for index in selected_indexes:
            row, col = index.row(), index.column()
            if row not in selected_data:
                selected_data[row] = {}
            selected_data[row][col] = model.data(index)

        # Convert selected data to a tab-delimited string
        rows = sorted(selected_data.keys())
        cols = sorted({col for row_data in selected_data.values() for col in row_data.keys()})
        
        clipboard_string = ""
        for row in rows:
            row_data = []
            for col in cols:
                row_data.append(selected_data[row].get(col, ""))
            clipboard_string += "\t".join(row_data) + "\n"

        # Copy to clipboard
        clipboard = QApplication.clipboard()
        clipboard.setText(clipboard_string)

          
    def paste_selected(self):
        active_table_view = self.get_active_tableview()
        if active_table_view is None:
            self.render_info_text("No active table view.")
            return

        clipboard = QApplication.clipboard()
        clipboard_text = clipboard.text()
        

        if not clipboard_text:
            self.render_info_text("Clipboard is empty.")
            return

        model = active_table_view.model()
        if model is None:
            model =  QStandardItemModel()
            active_table_view.setModel(model)

        # Parse clipboard text into a list of lists
        rows = clipboard_text.split("\n")
        data = [row.split("\t") for row in rows if row]
        
        
        # Check for selected rows and remove them
        selection_model = active_table_view.selectionModel()
        selection_model = active_table_view.selectionModel()
        if selection_model is None:
            self.render_info_text("Table view has no selection model.")
            return
                
        selected_indexes = selection_model.selectedRows()

        if selected_indexes:
            rows_to_remove = sorted([index.row() for index in selected_indexes], reverse=True)
            for row in rows_to_remove:
                model.removeRow(row)

        if not self.duplicates_check_box.isChecked():
            # Remove duplicate rows
            data = self.remove_duplicate_rows(data, active_table_view)

        # Append data to the table view
        for row_data in data:
            items = [ QStandardItem(field) for field in row_data]
            for item in items:
                item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)  # Make item non-editable if required
            model.appendRow(items)

        header = active_table_view.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)


    def export(self, scope, format):
        active_table_view = self.get_active_tableview()
        
        if self.is_tableview_empty(active_table_view):
            self.render_info_text("Please run a query first.")
            return

        if scope == 'all':
            results, columns = self.get_all_rows(active_table_view)
        elif scope == 'selection':
            results, columns = self.get_selected_rows(active_table_view)
            
            if not results or not columns:
                self.render_info_text("Please make a valid selection.")
                return        
    
        e = None
        file_dialog_filters = {
            'csv': "CSV Files (*.csv);;All Files (*)",
            'json': "JSON Files (*.json);;All Files (*)",
            'html': "HTML Files (*.html);;All Files (*)",
            'xml': "XML Files (*.xml);;All Files (*)",
            'excel': "Excel Files (*.xlsx);;All Files (*)",
            'parquet': "Parquet Files (*.parquet);;All Files (*)",
            'hdf5': "HDF5 Files (*.h5);;All Files (*)"
        }
        
        if format in file_dialog_filters:
            file_path, _ = QFileDialog.getSaveFileName(self, f"Save {format.upper()}", "", file_dialog_filters[format])
            if file_path:
                export_methods = {
                    'csv': self.main_app.exportToCSV,
                    'json': self.main_app.exportToJSON,
                    'html': self.main_app.exportToHTML,
                    'xml': self.main_app.exportToXML,
                    'excel': self.main_app.exportToEXCEL,
                    'parquet': self.main_app.exportToParquet,
                    'hdf5': self.main_app.exportToHDF5
                }
                e = export_methods[format](results, columns, file_path)
        
        if e is True:
            QMessageBox.information(self, "Success", "File was exported successfully.")
        elif e is not None:
            self.render_detailed_error_text(f"{e}")

    def get_selected_rows(self, table_view):

        selection_model = table_view.selectionModel()
        selected_rows = selection_model.selectedRows()

        # Get the model associated with the QTableView
        model = table_view.model()

        # Initialize results and columns
        selected_results = []
        selected_columns = [model.headerData(i, Qt.Orientation.Horizontal) for i in range(model.columnCount())]

        # Extract data from selected rows
        for row_index in selected_rows:
            row_data = []
            for column_index in range(model.columnCount()):
                index = model.index(row_index.row(), column_index)
                row_data.append(model.data(index))
            selected_results.append(row_data)
        
        return selected_results, selected_columns
    
    def get_all_rows(self, table_view):
        model = table_view.model()
        if model is None:
            return [], []

        results = []
        columns = [model.headerData(i, Qt.Orientation.Horizontal) for i in range(model.columnCount())]

        for row in range(model.rowCount()):
            row_data = []
            for column in range(model.columnCount()):
                index = model.index(row, column)
                row_data.append(model.data(index))
            results.append(row_data)

        return results, columns        

    def get_active_tableview(self):
        current_index = self.tab_widget.currentIndex()
        current_tab = self.tab_widget.widget(current_index)
        table_view = current_tab.findChild(QTableView)
        return table_view

    def set_window_style(self):
        self.setStyleSheet("""

            QLineEdit { padding: 5px;}
            QPushButton {  padding: 5px 10px;background-color: #007bff;color: white;border: none;border-radius: 5px;}
            QPushButton:hover {background-color: #0056b3;}

            QHeaderView::section {

            }
            QTableView {
                border: 1px solid #fff;
            }
        """)     

    def new_connection(self):
        self.main_app.close_db()
        from pySQLExport_gui.new_connection_window import NewConnectionWindow
        self.connection_window = NewConnectionWindow()
        self.connection_window.show()
        self.close()

    def exit_app(self):
        self.main_app.close_db()
        QApplication.quit()

    def retranslate_ui(self):
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "pySQLExport"))
        self.label_sql_query.setText(_translate("MainWindow", "Run Query:"))
        self.query_button.setText(_translate("MainWindow", "Execute Query"))
        #self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_1), _translate("MainWindow", "Query 1"))
        #self.tab_widget.setCurrentIndex(0)

    def run_query(self, query):
        if query:
            if self.new_tab_check_box.isChecked():
                self.add_new_tab()

            success, result_or_error, columns = self.main_app.execute_query(query)
            if success:
                results = result_or_error
                self.display_results(results, columns)
                self.text_sql_query.setPlainText("")
            else:
                self.render_error_text(f"Failed to execute query: {result_or_error}")
        else:
            self.render_info_text("Query cannot be empty.          ")

    def has_duplicate_rows(self, table_view: QTableView) -> tuple:
        model = table_view.model()
        if not model:
            return False, 0

        seen_rows = set()
        duplicate_count = 0

        # Check for duplicate row indices and count them
        for row in range(model.rowCount()):
            row_data = tuple(model.index(row, col).data() for col in range(model.columnCount()))
            if row_data in seen_rows:
                duplicate_count += 1
            else:
                seen_rows.add(row_data)

        return duplicate_count > 0, duplicate_count

    def remove_duplicate_rows(self, new_data, table_view: QTableView):
        model = table_view.model()
        if model is None:
            return new_data

        existing_rows = set()
        for row in range(model.rowCount()):
            row_data = tuple(model.data(model.index(row, col)) for col in range(model.columnCount()))
            existing_rows.add(row_data)

        cleaned_data = []
        for new_row in new_data:
            row_tuple = tuple(new_row)
            if row_tuple not in existing_rows:
                cleaned_data.append(new_row)
                existing_rows.add(row_tuple)

        return cleaned_data
    
    def remove_duplicate_from_tableview(self, table_view: QTableView):
        model = table_view.model()
        if not model:
            return

        seen_rows = set()
        duplicates = []

        # Collect duplicate row indices
        for row in range(model.rowCount()):
            row_data = tuple(model.index(row, col).data() for col in range(model.columnCount()))
            if row_data in seen_rows:
                duplicates.append(row)
            else:
                seen_rows.add(row_data)

        # Remove duplicates from bottom to top to prevent reindexing issues
        for row in reversed(duplicates):
            model.removeRow(row)
    
    def row_exists(self, model, new_row):
        for row in range(model.rowCount()):
            match = True
            for column in range(model.columnCount()):
                if model.item(row, column).text() != new_row[column].text():
                    match = False
                    break
            if match:
                return True
        return False
    
    def display_results(self, results, columns):
        table_view = self.get_active_tableview()  # Get the active table view
        model = table_view.model()

        if model is None or not self.append_check_box.isChecked():
            model = QStandardItemModel()
            model.setHorizontalHeaderLabels(columns)
            table_view.setModel(model)
        else:
            existing_columns = model.columnCount()
            for i, column in enumerate(columns):
                if i >= existing_columns:
                    model.setHorizontalHeaderItem(i, QStandardItem(column))
    
        for row in results:
            items = [QStandardItem(str(field)) for field in row]
            #for item in items:
            #    item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)  # Make item non-editable

            #if self.duplicates_check_box.isChecked():
            model.appendRow(items)
            #else:
             #   if not self.row_exists(model, items):
              #      model.appendRow(items) 

        header = table_view.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        duplicate, duplicate_count = self.has_duplicate_rows(table_view)
        if duplicate:
            remove_duplicates = self.ask_user('Remove Duplicates?', f'The query returned {duplicate_count} rows that already existed in the table view. Would you like to remove the duplicate items?')
            if remove_duplicates:
                self.remove_duplicate_from_tableview(table_view) 

