import streamlit as st
import pandas as pd
import numpy as np
#from prediction import predict
import joblib as jb

model = jb.load('rf_model.sav')

st.title('Predict salary base on education level')
st.text_input('input your id', '12345')

option = st.selectbox(
    'Enter your Education level',
    ('Diploma', 'Bachelors ', 'Masters', 'Doctorate', 'Professional'))

st.write('You selected:', option)

age = st.slider('How old are you?', 0, 130, 25)
st.write('your age is ', age)


def predict():
    education_levels = ['Diploma', 'Bachelors ',
                        'Masters', 'Doctorate', 'Professional']
    education_idx = education_levels.index(option)
    row = np.zeros(5)
    row[education_idx] = 1
    x = pd.DataFrame([row])
    x.columns = education_levels
    x.insert(0, 'Age', age)
    st.write(x)
    prediction = model.predict(x)[0]
    st.write(f"Your predicted salary is {prediction}")


but = st.button('Predict', on_click=predict())

"""  """
