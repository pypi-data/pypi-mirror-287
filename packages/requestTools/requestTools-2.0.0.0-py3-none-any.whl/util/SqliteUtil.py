import logging
import sqlite3
import pandas as pd

log = logging.getLogger(__name__)

class SqliteUtil:

    @staticmethod
    def import_excel_to_sqlite(
            excel_file_path: str,
            sheet_name: str,
            sqlite_db_path: str,
            table_name: str
    ):
        """
        Imports data from an Excel sheet into an SQLite database table.

        This method reads data from a specified sheet within an Excel file and writes it to
        a table in an SQLite database. If the table already exists, it will be replaced.

        :param excel_file_path: The path to the Excel file containing the data.
        :param sheet_name: The name of the sheet within the Excel file to read the data from.
        :param sqlite_db_path: The path to the SQLite database file.
        :param table_name: The name of the table in the SQLite database where the data will be inserted.

        :raises Exception: If an error occurs during the operation, it logs the exception message.
        """

        conn = None
        try:
            # Load the Excel data into a Pandas DataFrame
            df = pd.read_excel(excel_file_path, sheet_name=sheet_name)

            # Connect to the SQLite database
            conn = sqlite3.connect(sqlite_db_path)

            # Write the DataFrame data to the specified table in SQLite
            df.to_sql(table_name, conn, index=False, if_exists='replace')

            # Log success message
            log.info(f"Data imported successfully into {table_name}.")
        except Exception as e:
            # Log any exceptions that occur
            log.info(f"An error occurred: {e}")
        finally:
            # Close the database connection
            if conn is not None:
                conn.close()



