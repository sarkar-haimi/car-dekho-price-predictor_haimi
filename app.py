import streamlit as st
import numpy as np
import pandas as pd
import pickle


pipe=pickle.load(open('pipe.pkl','rb'))

st.header('Car Price Predictor')

# year
year=st.number_input('Manufacturing year of car',2000,2020)
# km driven
km_driven=st.number_input('KMs driven')
# fuel
fuel=st.selectbox('Select Fuel type',('Diesel','Petrol'))
# seller type
seller_type=st.selectbox('Select Seller type',('Individual','Dealer'))
# transmission
transmission=st.selectbox('Select Transmission',('Manual','Automatic'))
# owner
owner=st.selectbox('Select owner type',('First Owner','Second Owner','Third Owner'))
# mileage
mileage=st.number_input('Mileage')
# engine
engine=st.number_input('Engine')
# max power
max_power=st.number_input('Max Power')
# seats
seats=st.number_input('Seats')
# brand
brand=st.selectbox('Select Brand of car',('Maruti','Hyundai','Mahindra',
                                          'Tata','Honda','Ford','Toyota','Chevrolet','Renault','Volkswagen'))

if st.button('Predict Price'):
    # form a numpy array
    input=np.array([[year,km_driven,fuel,seller_type,transmission,owner,mileage,engine,max_power,seats,brand]])
    input=pd.DataFrame(input,columns=['year','km_driven','fuel','seller_type','transmission',
                                      'owner','mileage','engine','max_power','seats','brand'])
    #st.dataframe(input)
    y_pred=pipe.predict(input)
    st.title("Rs " + str(np.round(y_pred[0])))