from fileinput import filename
import pyarrow as pv
import pyarrow.parquet as pq
import pandas as pd
import os



class parquetFile (object):
    def __init__(self, file, sheet) -> None:
        self.file = file
        self.sheet = sheet

    def excel_to_parquet(self):
        data = pd.read_excel(self.file, engine='openpyxl', sheet_name =self.sheet )
        table = pv.Table.from_pandas(data)
        pq.write_table(table, self.file+'.parquet')


current_dir = os.getcwd()
list_of_files = os.listdir(current_dir)


file_sheet = []

for file in list_of_files:
    if file.lower().endswith((".xlsx",".xls")):
        sheets = pd.ExcelFile(file).sheet_names
        for sheet in sheets:
            file_sheet.extend([{file : sheet}])


for index, i in enumerate(file_sheet):
        for file_name in i.keys():
            for sheet_name in i.values():
                first_file = parquetFile(file_name, sheet_name)
                first_file.excel_to_parquet()


