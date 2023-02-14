import numpy as np
import streamlit as st
import pickle


# loading the saved model
loaded_model = pickle.load(open('C:/Users/swesh/OneDrive/Desktop/Diabetes_Prediction/trained_model.sav', 'rb'))


def diabetes_prediction(input_data):

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The person is not diabetic'
    else:
       return 'The person is diabetic'

def main():
    st.title('LordVoldemort presents-')
    st.title('Diabetes Prediction web App')
    
    
    
    Pregnancies=st.text_input('Number of Pregnancies')
    Glucose=st.text_input('glucose level')
    BloodPressure=st.text_input('BP value')
    SkinThickness=st.text_input('skin Thickness')
    Insulin=st.text_input('insulin value')
    BMI=st.text_input('BMI value')
    DiabetesPedigreeFunction=st.text_input('Diabetes Pedigree Function value')
    Age=st.text_input('Age')
    
    dignosis=''
    
    if st.button('Diabetes Test Results'):
        dignosis=diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
    
    st.success(dignosis)
    
    
if __name__=='__main__':
    main()    
    
    
    
    
    