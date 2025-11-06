import streamlit as st 

st.title("BMI Calculator")

weight = st.number_input("Enter your weight (kg):", format="%.2f")
height_unit = st.radio("Select height unit:", ["cm", "m", "ft"])
height = st.number_input(f"Enter your height in {height_unit}:", format="%.2f")

if st.button("Calculate"):
    try:
        if height_unit == "cm":
            height /= 100 
        elif height_unit == "ft":
            height /= 3.28 
        
        if height <= 0:
            st.error("Height must be greater than 0")
        else:
            bmi = weight / (height ** 2)
            st.success(f"your bmi is {bmi:.2f}")

            if bmi < 17:
                st.error("extremeley underweight")
            elif 17 <= bmi < 18.5:
                st.warning("underweight")
            elif 18.5 <= bmi < 25:
                st.success("healthy boi")
            elif 25 <= bmi < 30:
                st.warning("overweight")
            else:
                st.error("wtf fatty")

    except:
        st.error("Please enter valid numbers")

