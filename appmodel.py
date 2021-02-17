import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle


df = pd.read_csv("final_df.csv")

X=df.drop(['Rent_transform','Price_per_sqft'],axis=1)
y=df.Rent_transform

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=51)

model = pickle.load(open("rent_rfr_new.pkl","rb"))

def predict_price(location,facing,water,typ,area,balcony,age,parking,bhk,security,bathroom,furnishing):    
    loc_index = np.where(X.columns==location)[0][0]
    facing_index = np.where(X.columns==facing)[0][0]
    water_index = np.where(X.columns==water)[0][0]
    typ_index = np.where(X.columns==typ)[0][0]

    x = np.zeros(len(X.columns))
    x[33] = area
    x[32] = balcony
    x[31] = age
    x[30] = parking
    x[29] = bhk
    x[28] = security
    x[27] = bathroom
    x[26] = furnishing
    
    if loc_index >= 0:
        x[loc_index] = 1
        
        
    if facing_index >= 0:
        x[facing_index] = 1

    if water_index >= 0:
        x[water_index] = 1

    if typ_index >= 0:
        x[water_index] = 1  
        
    Rent_lambda= 0.16817476247598015
    predict = model.predict([x])[0]
    predict_price = predict**2

    return int(predict_price)
