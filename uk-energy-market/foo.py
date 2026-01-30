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


fdir = "C:\\Users\\samee\\Desktop\\py-projects\\other\\electricity\\datasets\\"
files = [f for f in os.listdir(fdir)]

reader = FileReader(fdir, files[0])

def fetch_series(period):
    # daily series (7 day avg)
    df_daily = reader.read(3, 3)
    df_daily.set_index("Date", inplace=True)

    # monthly series
    df_monthly = reader.read(4, 4)
    df_monthly.set_index("Date", inplace=True)

    return df_daily if period == "daily" else df_monthly
