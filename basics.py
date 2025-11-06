import streamlit as st 
from PIL import Image

# text
st.title("Hello world!")
st.header("This is a header")
st.subheader("this is a subheader")
st.text("how now brown cow. what say you. etc etc.")
st.markdown("### This is markdown text wow")

# logging / status messages
st.info("5 jobs scheduled today")
st.success("1 job completes successfully!")
st.warning("2 jobs need reviewing")
st.error("oh no please look into these things immediately!")
exp = ZeroDivisionError("trying to divide by zero nono")
st.exception(exp)

# writing anything (not just text)
st.write([n for n in range(5)])

# images and checkboxes
img = Image.open("images/afc.jpg")
if st.checkbox("Show / Hide Image"):
    st.image(img, width=300)

# radio buttons
status = st.radio("Select Gender: ", ["Male", "Female"]) 
if status == "Male":
    st.success("Male")
else:
    st.success("Female")

# dropdowns 
hobby = st.selectbox("Select a hobby:", ["dancing", "reading", "sports"])
st.write("your hobby is ", hobby)

# multi selection
hobbies = st.multiselect("Select your hobbies:", ["dancing", "sports", "reading"])
st.write("you select ", len(hobbies), " hobbies:", hobbies)

# buttons
button = st.button("hey! click me")
if button:
    st.text("excellent work")

# user input
name = st.text_input(label="Enter your name:", placeholder="Type here...")
if st.button("submit"):
    result = name.title() 
    st.success(result)

# sliders
level = st.slider("Choose a level", min_value=1, max_value=10)
st.write("Selected level: ", level)
