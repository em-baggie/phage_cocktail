# module for loading excel files
#create data_loader class

import polars as pl

#initialise class
class DataLoader:
    def __init__(self, file_path, sheet_name):
        self.file_path = file_path
        self.sheet_name = sheet_name

    def load_data(self):
        return pl.read_excel(
            source = self.file_path,
            sheet_name = self.sheet_name,
            engine = "calamine"
        )

#test
file_path = "all_host_range.xlsx"
sheet_name = "test"

loader = DataLoader(file_path, sheet_name)
data_frame = loader.load_data()

print(data_frame)