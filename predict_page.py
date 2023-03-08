import pandas as pd
import numpy as np
import streamlit  as st
import pickle
import sklearn as sns
import seaborn as sns
import datetime
 

def load_model():

    with open("flight_rf .pkl",'rb') as file:
        data = pickle.load(file)
    return data

data  =load_model()

def show_page():
    
    st.title("Flight Price Predicter")

    from PIL import Image
    image = Image.open('1608318032-013.webp')

    st.image(image, caption='All journeys have secret destinations of which the traveler is unaware')

    st.write("""### Please Enter following details""")

    airline = (
        'IndiGo', 'Air India', 'Jet Airways', 'SpiceJet',
       'Multiple carriers', 'GoAir', 'Vistara', 'Air Asia',
       'Vistara Premium economy', 'Jet Airways Business',
       'Multiple carriers Premium economy')

    destination = (
        'New Delhi', 'Banglore', 'Cochin', 'Kolkata', 'Delhi', 'Hyderabad'
    )

    source = (
        'Banglore', 'Kolkata', 'Delhi', 'Chennai', 'Mumbai'
    )

    Airline = st.selectbox("Airline" , airline)
  
    Source = st.selectbox("Source" , source)
    Destination = st.selectbox("Destination" , destination)
    departure_date = st.date_input(label="Departure Date")
    arival_date = st.date_input(label="Arival Date")
    departure_time = st.time_input(label="Departure Time")
    arrival_time = st.time_input(label="Arrival Time")

    num_of_stop = st.number_input("Number Of Stops",1,10,1)
    ok = st.button("Predict Price")
    if ok:
        Total_Stops = int(num_of_stop)
        Journey_Day = pd.to_datetime(departure_date,format = "%Y-%m-%dT%H:%M").day
        Journey_month = pd.to_datetime(departure_date,format = "%Y-%m-%dT%H:%M").month
        Dep_hour = int(departure_time.hour)
        Dep_min =  int(departure_time.minute)
        Arr_hour = int(arrival_time.hour)
        Arr_min =  int(arrival_time.minute)
        if Dep_hour>Arr_hour:
            duration_hour=abs(24-(Dep_hour - Arr_hour))
        else:
            duration_hour = (Dep_hour - Arr_hour)
        
        duration_min=abs(int(Dep_min) - int(Arr_min))

        Airline_Air_India = 0
        Airline_GoAir = 0
        Airline_IndiGo = 0
        Airline_Jet_Airways = 0
        Airline_Jet_Airways_Business = 0
        Airline_Multiple_carriers = 0
        Airline_Multiple_carriers_Premium_economy = 0
        Airline_SpiceJet = 0
        Airline_Vistara = 0
        Airline_Vistara_Premium_economy = 0


        Source_Chennai = 0
        Source_Delhi = 0
        Source_Kolkata = 0
        Source_Mumbai = 0


        Destination_Cochin = 0
        Destination_Delhi = 1
        Destination_Hyderabad = 0
        Destination_Kolkata = 0
        Destination_New_Delhi = 0 







        if Airline == "Air India":
            Airline_Air_India = 1
            Airline_GoAir = 0
            Airline_IndiGo = 0
            Airline_Jet_Airways = 0
            Airline_Jet_Airways_Business = 0
            Airline_Multiple_carriers = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_Vistara_Premium_economy = 0
        if Airline == "GoAir":
            Airline_Air_India =0
            Airline_GoAir = 1
            Airline_IndiGo = 0
            Airline_Jet_Airways = 0
            Airline_Jet_Airways_Business = 0
            Airline_Multiple_carriers = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_Vistara_Premium_economy = 0
        if Airline == "IndoGo":
            Airline_Air_India =0
            Airline_GoAir = 0
            Airline_IndiGo = 1
            Airline_Jet_Airways = 0
            Airline_Jet_Airways_Business = 0
            Airline_Multiple_carriers = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_Vistara_Premium_economy = 0
        if Airline == "Jet Airways":
            Airline_Air_India =0
            Airline_GoAir = 0
            Airline_IndiGo = 0
            Airline_Jet_Airways = 1
            Airline_Jet_Airways_Business = 0
            Airline_Multiple_carriers = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_Vistara_Premium_economy = 0
        if Airline == "Jet Airways Business":
            Airline_Air_India =0
            Airline_GoAir = 0
            Airline_IndiGo = 0
            Airline_Jet_Airways = 0
            Airline_Jet_Airways_Business = 1
            Airline_Multiple_carriers = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_Vistara_Premium_economy = 0
        if Airline == "Multiple carriers Premium economy":
            Airline_Air_India =0
            Airline_GoAir = 0
            Airline_IndiGo = 0
            Airline_Jet_Airways = 0
            Airline_Jet_Airways_Business = 0
            Airline_Multiple_carriers = 0
            Airline_Multiple_carriers_Premium_economy = 1
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_Vistara_Premium_economy = 0
        if Airline == "SpiceJet":
            Airline_Air_India =0
            Airline_GoAir = 0
            Airline_IndiGo = 0
            Airline_Jet_Airways = 0
            Airline_Jet_Airways_Business = 0
            Airline_Multiple_carriers = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_SpiceJet = 1
            Airline_Vistara = 0
            Airline_Vistara_Premium_economy = 0
        if Airline == "Vistara":
            Airline_Air_India =0
            Airline_GoAir = 0
            Airline_IndiGo = 0
            Airline_Jet_Airways = 0
            Airline_Jet_Airways_Business = 0
            Airline_Multiple_carriers = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 1
            Airline_Vistara_Premium_economy = 0
        if Airline == "Vistara Premium economy":
            Airline_Air_India =0
            Airline_GoAir = 0
            Airline_IndiGo = 0
            Airline_Jet_Airways = 0
            Airline_Jet_Airways_Business = 0
            Airline_Multiple_carriers = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_Vistara_Premium_economy = 1

        if Source == "Chennai":
            Source_Chennai = 1
            Source_Delhi = 0
            Source_Kolkata = 0
            Source_Mumbai = 0
        if Source == "Delhi":
            Source_Chennai = 0
            Source_Delhi = 1
            Source_Kolkata = 0
            Source_Mumbai = 0
        if Source == "Kolkata":
            Source_Chennai = 0
            Source_Delhi = 0
            Source_Kolkata = 1
            Source_Mumbai = 0
        if Source == "Mumbai":
            Source_Chennai = 0
            Source_Delhi = 0
            Source_Kolkata = 0
            Source_Mumbai = 1
        if Destination =="Cochin": 
            Destination_Cochin = 1
            Destination_Delhi = 0
            Destination_Hyderabad = 0
            Destination_Kolkata = 0
            Destination_New_Delhi = 0 
        if Destination =="Delhi":
            Destination_Cochin = 0
            Destination_Delhi = 1
            Destination_Hyderabad = 0
            Destination_Kolkata = 0
            Destination_New_Delhi = 0 
        if Destination =="Hyderabad":
            Destination_Cochin = 0
            Destination_Delhi = 0
            Destination_Hyderabad = 1
            Destination_Kolkata = 0
            Destination_New_Delhi = 0 
        if Destination =="Kolkata":
            Destination_Cochin = 0
            Destination_Delhi = 0
            Destination_Hyderabad = 0
            Destination_Kolkata = 1
            Destination_New_Delhi = 0 
        if Destination =="New Delhi":
            Destination_Cochin = 0
            Destination_Delhi = 0
            Destination_Hyderabad = 0
            Destination_Kolkata = 0
            Destination_New_Delhi = 1 
        x = np.array([[Total_Stops,Journey_Day,Journey_month,Dep_hour,Dep_min,Arr_hour,
               Arr_min,duration_hour,duration_min,
               Airline_Air_India,Airline_GoAir,
               Airline_IndiGo,Airline_Jet_Airways,Airline_Jet_Airways_Business,Airline_Multiple_carriers,
               Airline_Multiple_carriers_Premium_economy
               ,Airline_SpiceJet,Airline_Vistara,
               Airline_Vistara_Premium_economy,
               Source_Chennai,Source_Delhi,Source_Kolkata,
             Source_Mumbai,Destination_Cochin,
           Destination_Delhi,Destination_Hyderabad,
               Destination_Kolkata,Destination_New_Delhi]])
        
        Price = data.predict(x)
        st.subheader(f"The estimated price is {Price[0]:.2f} Rupees")

    
            






     
     
         

 