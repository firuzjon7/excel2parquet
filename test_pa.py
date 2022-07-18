from fileinput import filename
import pyarrow as pv
import pyarrow.parquet as pq
import pandas as pd




class parquetFile (object):
    def __init__(self, file, sheet) -> None:
        self.file = file
        self.sheet = sheet

    def excel_to_parquet(self):
        data = pd.read_excel(self.file, engine='openpyxl', sheet_name =self.sheet )
        table = pv.Table.from_pandas(data)
        pq.write_table(table, self.file+'.parquet')

file = 'test_schema2.xlsx'
sheet = 'Tabelle1'



first_file = parquetFile(file, sheet)

first_file.excel_to_parquet()


