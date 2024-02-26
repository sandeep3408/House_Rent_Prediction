import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.title("House Rent Prediction")

pickle_in = open("predict.pkl","rb")

model = pickle.load(pickle_in)

df = pd.read_csv('hyd_v2.csv')

X = pd.read_csv('da.csv')

x = df.columns

l = ['A S Rao Nagar',
 'Adibatla',
 'Adikmet',
 'Almasguda',
 'Alwal',
 'Amberpet',
 'Ameerpet',
 'Annojiguda',
 'Attapur',
 'B N Reddy Nagar',
 'Bachupally',
 'Badangpet',
 'Bahadurguda',
 'Balanagar',
 'Balapur',
 'Balkampet',
 'Bandlaguda',
 'Banjara Hills',
 'Basheer Bagh',
 'Beeramguda',
 'Begumpet',
 'Bharat Heavy Electricals Limited',
 'Bhoiguda',
 'Boduppal',
 'Bolarum',
 'Borabanda',
 'Bowenpally',
 'Bowrampet',
 'Champapet',
 'Chandanagar',
 'Chikkadpally',
 'Chintal',
 'Chintalmet',
 'Dilsukhnagar',
 'East Marredpally',
 'Erragadda',
 'Film Nagar',
 'Gachibowli',
 'Gajularamaram',
 'Gokul Plats',
 'Gopanpally',
 'Gudimalkapur',
 'HITEC City',
 'Habsiguda',
 'Hafeezpet',
 'Hakimpet',
 'Hastinapuram',
 'Hayathnagar',
 'Himayatnagar',
 'Hyderabad',
 'Hyderguda',
 'Hydernagar',
 'Hydershakote',
 'Jagathgiri Gutta',
 'Jawahar Nagar',
 'Jeedimetla',
 'Jillelaguda',
 'Jubilee Hills',
 'Kachiguda',
 'Kamalaprasad Nagar',
 'Kapra',
 'Karkhana',
 'Karmanghat',
 'Kavadiguda',
 'Khairatabad',
 'Khajaguda',
 'Kismatpur',
 'Kistareddypet',
 'Kokapet',
 'Kompally',
 'Kondapur',
 'Kothaguda',
 'Kothapet',
 'Krishna Reddy Pet',
 'Kukatpally',
 'Kushaiguda',
 'LB Nagar',
 'Lakdikapul',
 'Langar Houz',
 'Lingampally',
 'Madeenaguda',
 'Madhapur',
 'Madhura Nagar',
 'Madinaguda',
 'Malakpet',
 'Malkajgiri',
 'Mallampet',
 'Mallapur',
 'Manikonda',
 'Mansoorabad',
 'Masab Tank',
 'Medipally',
 'Meerpet',
 'Mehdipatnam',
 'Mettuguda',
 'Miyapur',
 'Moosapet',
 'Moti Nagar',
 'Moula Ali',
 'Musheerabad',
 'Nacharam',
 'Nagaram',
 'Nagole',
 'Nallagandla',
 'Nallakunta',
 'Nampally',
 'Nanakaramguda',
 'Narayanguda',
 'Narsingi',
 'Neknampur',
 'Neredmet',
 'New Nallakunta',
 'Nizampet',
 'Old Bowenpally',
 'Osman Nagar',
 'Padmarao Nagar',
 'Patancheru',
 'Peeramcheru',
 'Peerzadiguda',
 'Pocharam',
 'Punjagutta',
 'Puppalaguda',
 'Puppalguda',
 'Quthbullapur',
 'Qutub Shahi Tombs',
 'Rajendranagar Mandal',
 'Ram Nagar',
 'RamNaresh Nagar',
 'Ramachandrapuram',
 'Ramanthapur',
 'Rampally',
 'Rasoolpura',
 'Rodamestri Nagar',
 'Safilguda',
 'Saidabad',
 'Sainikpuri',
 'Sanath Nagar',
 'Sanjeeva Reddy Nagar',
 'Saroornagar',
 'Secunderabad',
 'Serilingampally',
 'Shaikpet',
 'Shamshabad',
 'Shilpa Hills',
 'Shivaji Nagar',
 'Somajiguda',
 'Suraram',
 'Tarnaka',
 'Tellapur',
 'Toli Chowki',
 'Trimulgherry',
 'Turkayamjal',
 'Uppal',
 'Upparpally',
 'Vanasthalipuram',
 'Warasiguda',
 'West Marredpally',
 'Whisper Valley',
 'Whitefields',
 'Yapral',
 'Yella Reddy Guda',
 'Yousufguda',
 'Zamistanpur']

b = ['BHK1',
 'BHK2',
 'BHK3',
 'BHK4',
 'BHK4PLUS']

f = [ 'Full',
 'Semi',]

loc = st.selectbox('Enter Location',l,index=0)

bhk = st.selectbox("Select BHK",b,index=0)

furnish = st.selectbox('Select Furnishing',f,index=0)

bath = st.text_input("Enter No Of Bathrooms")

property = st.text_input('Enter Property Size')



def predict(location, bhk, furnishing, bathroom, propertysize):

    X_columns = X.columns 
    
    print("X_columns:", X_columns) 
    
    furnish_index = np.where(X_columns == furnishing)[0][0]
    bhk_index = np.where(X_columns == bhk)[0][0]
    loc_index = np.where(X_columns == location)[0][0]
    
    print("Furnish index:", furnish_index)  
    print("BHK index:", bhk_index)          
    print("Location index:", loc_index)      
    
    x = np.zeros(len(X_columns)-41)
    
    x[0] = bathroom
    x[1] = propertysize
    
    print("Initial x:", x)  
    
    if furnish_index >= 0 and furnish_index < len(x):
        x[furnish_index] = 1
    
    if bhk_index >= 0 and bhk_index < len(x):
        x[bhk_index] = 1
    
    if loc_index >= 0 and loc_index < len(x):
        x[loc_index] = 1
    
    print("Final x:", x)  
    
    return model.predict([x])[0]

result = ''

if st.button('Predict Rent Price'):
    result = predict(loc, bhk, furnish, bath, property)
    st.write(result)

st.success('The Predicted Rent Price Is {}'.format(result))



