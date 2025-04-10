import streamlit as st

st.title("BMI Calculator")
st.write("Calculate your Body Mass Index (BMI)")

weight = st.number_input("Enter your weight (kg)")
height = st.number_input("Enter your height (cm)")


calculate_button = st.button("Calculate BMI")
if calculate_button:
    if weight > 0 and height > 0:
        bmi = weight / ((height / 100) ** 2) # Convert height to meters
        st.write(f"#### Your BMI is: {bmi:.2f} ####")
        if bmi < 18.5:
            st.write("##### You are underweight. #####")
        elif 18.5 <= bmi < 24.9:
            st.write("##### You have a normal weight. #####")
        elif 25 <= bmi < 29.9:
            st.write("##### You are overweight. #####")
        else:
            st.write("##### You are obese. #####")
    else:
        st.error("Please enter valid weight and height values.")

    st.write("## BMI Categories: ##")
    st.write("Underweight: BMI < 18.5")
    st.write("Normal weight: BMI 18.5 - 24.9")
    st.write("Overweight: BMI 25 - 29.9")
    st.write("Obesity: BMI ≥ 30")
    st.write("For more information, please consult a healthcare professional.")
    st.write("This app is for educational purposes only and should not be used as a substitute for professional medical advice.")
