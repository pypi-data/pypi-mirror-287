from pySQLExport_gui.database import get_database
import pandas as pd
from pandas.errors import ParserError



class PySQLExport:
    def __init__(self):
        self.config = {}
        self.error = None
        self.db = None
        self.version = '0.1.0'

    def connect_db(self, db_type, host, user, pw, database, port):
        self.config = {
            "db_type": db_type,
            "host": host,
            "user": user,
            "pass": pw,
            "port": port,
            "database": database
        }
        try:
            self.db = get_database(db_type, host, user, pw, database, port)
            return True
        except Exception as e:
            self.error = e
            return False
        
    def execute_query(self, query):
        try:
            self.results,  self.columns = self.db.execute(query)
            return True, self.results, self.columns
        except Exception as e:
            print(f"Failed to execute query: {e}")
            return False, str(e), []


        
    def close_db(self):
        self.db.close()

    def exportToCSV(self, results, columns, outfile):        
        df = pd.DataFrame(results, columns=columns)
        try:
            df.to_csv(outfile, index=False)
            return True
        except Exception as e:
            self.error = f"Failed to export to CSV: {e}"
            return e

    def exportToJSON(self, results, columns, outfile):        
        df = pd.DataFrame(results, columns=columns)
        try:
            df.to_json(outfile, orient='records', lines=True)
            return True
        except Exception as e:
            self.error = f"Failed to export to JSON: {e}"
            return e    
        
    def exportToXML(self, results, columns, outfile):        
        df = pd.DataFrame(results, columns=columns)
        try:
            df.to_xml(outfile, index=False, parser='lxml')
            return True
        except ImportError:
            df.to_xml(outfile, index=False, parser='etree')
            return True
        except Exception as e:
            self.error = f"Failed to export to XML: {e}"
            return e


    def exportToHTML(self, results, columns, outfile):        
        df = pd.DataFrame(results, columns=columns)
        try:
            df.to_html(outfile, index=False)
            return True
        except Exception as e:
            self.error = f"Failed to export to HTML: {e}"
            return e            
        
    def exportToEXCEL(self, results, columns, outfile):
        df = pd.DataFrame(results, columns=columns)
        try:
            df.to_excel(outfile, index=False, sheet_name='Sheet1')
            return True
        except Exception as e:
            self.error = f"Failed to export to Excel: {e}"
            return e

