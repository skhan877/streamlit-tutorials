import sys, os
sys.path.append(os.path.abspath('..'))
from foo import *
import streamlit as st


# Begin building streamlit page
st.header("UK Energy Market Analysis")
# st.sidebar.success("Stuff here")

df_daily = fetch_series("daily")
df_monthly = fetch_series("monthly")

# plots
fig, ax = plt.subplots(figsize=(15, 8))
ax.plot(df_daily["7-day average"], label="7-day average")
ax.plot(df_monthly, label="Monthly Average", color="red")
ax.set_title("System Price of Electricity")
ax.legend()
st.pyplot(fig)
