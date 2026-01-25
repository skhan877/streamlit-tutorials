import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import os


class FileReader:
    def __init__(self, fpath, fname):
        self.fpath = fpath
        self.fname = fname
        self.dot = fname.find(".")
        self.extension = fname[self.dot:].lower()
        self.file = os.path.join(self.fpath, self.fname)

    def read(self, sheet_name, header):
        if self.extension == ".csv":
            return pd.read_csv(self.file)
        elif self.extension == ".xlsx":
            return pd.read_excel(self.file, sheet_name=sheet_name, header=header)


if __name__ == "__main__":
    fdir = "C:\\Users\\samee\\Desktop\\py-projects\\other\\electricity\\datasets\\"
    files = [f for f in os.listdir(fdir)]

    reader = FileReader(fdir, files[0])
    df = reader.read(3, 3)

    print(df.head(10))


"""
df_daily = pd.read_excel(fdir+files[0], sheet_name=3, header=3)
df_monthly = pd.read_excel(fdir+files[0], sheet_name=4)

df_daily.set_index("Date", inplace=True)
# df_daily.plot()
# plt.show()

st.title("Energy Market Analysis")
"""




