from typing import List, Dict

import pandas as pd
from openpyxl import load_workbook
from pandas import DataFrame


class XlsxUtil:
    """
    A utility class for handling operations related to Excel files.
    """

    @staticmethod
    def saveExcel(path:str,fileName:str,datas:Dict[str,List] = None,df:DataFrame = None ):
        """
        Save data to an Excel file.

        This method allows saving data either from a dictionary of lists or a pandas DataFrame to an Excel file.
        If both 'datas' and 'df' are provided, 'datas' will be used to create the DataFrame.

        Parameters:
        - path (str): The directory path where the Excel file will be saved.
        - fileName (str): The name of the Excel file (do not include the '.xlsx' extension).
        - datas (Dict[str, List], optional): A dictionary where keys are column names and values are lists of column values. Default is None.
        - df (DataFrame, optional): A pandas DataFrame to be saved to the Excel file. Default is None.

        Raises:
        - ValueError: If both 'datas' and 'df' are None, indicating there is no data to save.

        Returns:
        None

        Example usage:
        ```
        # Using a dictionary of lists
        data_dict = {
            'Column1': [1, 2, 3],
            'Column2': ['A', 'B', 'C']
        }
        MyClass.saveExcel('/path/to/save/', 'example', datas=data_dict)

        # Using an existing DataFrame
        import pandas as pd
        df = pd.DataFrame(data_dict)
        MyClass.saveExcel('/path/to/save/', 'example', df=df)
        ```
        Notes:
        - This method will save the data to a sheet named 'sheet0' by default.
        - After saving, the method will automatically adjust the column widths in the Excel file using the `XlsxUtil.auto_adjust_column_widths` method.
        """

        if datas is None and df is None:
            raise ValueError("At least one of the parameters must be non-null")

        fullFileName = path + fileName + '.xlsx'
        default_sheet_name = 'sheet0'
        if datas is not None:
            df = pd.DataFrame(datas)

        df.to_excel(fullFileName,sheet_name=default_sheet_name, index=False)

        XlsxUtil.auto_adjust_column_widths(fullFileName)


    @staticmethod
    def auto_adjust_column_widths(fullFileName):
        """
        Automatically adjusts the column widths of an Excel worksheet to fit the content.

        This method opens the specified Excel file, iterates over all columns
        and calculates the maximum length of the content in each column.
        It then adjusts the width of each column based on this maximum length
        to ensure that all content fits within the column's width when viewed.

        Parameters:
        fullFileName (str): The full path to the Excel file that needs to be adjusted.

        Example:
        auto_adjust_column_widths("path/to/your/excel_file.xlsx")
        """
        wb = load_workbook(fullFileName)
        ws = wb.active
        for col in ws.columns:
            max_length = 0
            column = col[0].column_letter  # 获取列字母
            for cell in col:
                try:
                    if len(str(cell.value)) > max_length:
                        max_length = len(str(cell.value))
                except:
                    pass
            adjusted_width = (max_length + 2)
            ws.column_dimensions[column].width = adjusted_width
        wb.save(fullFileName)



