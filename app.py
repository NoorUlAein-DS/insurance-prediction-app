import streamlit as st
import pickle
import pandas as pd

with open('insurance_model_by_Aein.pkl','rb')as file:
  model=pickle.load(file)
st.title('Insurance Charges Prediction')
st.divider()

age=st.slider('seect your age')
gender=st.selectbox('gender:',['Male','Female'])
bmi=st.number_input('BMI  body mass index',min_value=10, max_value=60, value=25)
children=st.selectbox('children',[0,1,2,3,4,5])
smoker=st.selectbox('Do you smoke?',['No','Yes'])
region = st.selectbox(" select your  Region :", ["Northeast", "Northwest", "Southeast", "Southwest"])

# Inputs ko numbers mein convert karna
is_Female = 1 if gender == "Female" else 0
is_smoker = 1 if smoker == "Yes" else 0

region_northwest = 1 if region == "Northwest" else 0
region_southeast = 1 if region == "Southeast" else 0
region_southwest = 1 if region == "Southwest" else 0

# Predict Button
if st.button("Predict Insurance Charges"):
    user_data = pd.DataFrame([{
        'age': age,
        'is_Female': is_Female,
        'bmi': int(bmi),
        'children': children,
        'is_smoker': is_smoker,
        'region_northwest': region_northwest,
        'region_southeast': region_southeast,
        'region_southwest': region_southwest
    }])

    prediction = model.predict(user_data)
    st.success(f" Estimated Annual Charges: ${prediction[0]:,.2f}")

