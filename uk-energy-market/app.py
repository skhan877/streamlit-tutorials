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

def main():
    fdir = "C:\\Users\\samee\\Desktop\\py-projects\\other\\electricity\\datasets\\"
    files = [f for f in os.listdir(fdir)]

    reader = FileReader(fdir, files[0])
    df_daily = reader.read(3, 3)
    df_monthly = reader.read(4, 4)

    df_daily_meta = reader.read(sheet_name=0, header=0)
    # print(df_daily_meta.head())
    # print(df_monthly.head(10))

    st.title("UK Energy Market Analysis")

    df_daily.set_index("Date", inplace=True)

    fig, ax = plt.subplots(figsize=(15, 8))
    ax.plot(df_daily["7-day average"], label="7-day average")
    ax.set_title("System Price of Electricity")
    ax.legend()
    st.pyplot(fig)


if __name__ == "__main__":
    main()



