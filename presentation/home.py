import streamlit as st

st.set_page_config(
    page_title="Portfolio App",
    page_icon="📊",
    layout="wide"
)

st.title("📊 My Data Portfolio")
st.subheader("Welcome to my professional project showcase")

st.markdown("""
This multi-page application highlights my professional journey and showcases a structured 
presentation of one of my completed projects.  
Use the navigation sidebar to browse through the content.
""")

st.divider()

st.markdown("### 🔍 Pages Included:")
st.markdown("""
- **About Me**  
- **Problem Statement**  
- **Methodology**  
- **Actions & Outcome**  
""")

st.divider()

st.markdown("Thank you for visiting! 🙌")
