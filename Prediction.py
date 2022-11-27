import pandas as pd
from sklearn.linear_model import LogisticRegression
import streamlit as st
import joblib

st.header("Streamlit Machine Learning App")

df = pd.read_csv("Road Quality.csv")

X = df[["Resource Access Roads (in km)", "Low traffic Roads(1 or 0)", " Low Speed Roads(m/s)", "Speed Range Roads(m/s)", "Land use Roads(in Km)", "Special Functional Roads (in km)", "Vehicle type Roads(in cm)", "Other PGMSY Roads (in Km)", "Special Section Roads (in Km)", "Weather Roads(in C)", "Junction Links(in Km)", "Streets(in Km)", "Path Holes (in Binary)"]]
y = df["Road Quality (G/B)"]

clf = LogisticRegression() 
clf.fit(X, y)
joblib.dump(clf, "clf.pkl")

a = st.number_input("Enter the Resource Access Road")
b = st.number_input("Enter the Low Traffic Roads")
c = st.number_input("Enter the Low Speed Roads ")
d = st.number_input("Enter the Speed Range Roads ")
e = st.number_input("Enter the Land Use Roads ")
f = st.number_input("Enter the Special Functional Roads ")
g = st.number_input("Enter the Vehicle Type Roads ")
h = st.number_input("Enter the Other PGMSY Roads ")
i = st.number_input("Enter the Special Section Roads ")
j = st.number_input("Enter the Weather Roads")
k = st.number_input("Enter the Junction Links ")
l = st.number_input("Enter the Streets")
m = st.number_input("Enter the Path Holes ")

if st.button("Submit"):
    
    # Unpickle classifier
    clf = joblib.load("clf.pkl")
    
    # Store inputs into dataframe
    X = pd.DataFrame([[a, b, c, d, e, f, g, h, i, j, k, l, m]], 
                     columns = ["Resource Access Roads (in km)", "Low traffic Roads(1 or 0)", " Low Speed Roads(m/s)", "Speed Range Roads(m/s)", "Land use Roads(in Km)", "Special Functional Roads (in km)", "Vehicle type Roads(in cm)", "Other PGMSY Roads (in Km)", "Special Section Roads (in Km)", "Weather Roads(in C)", "Junction Links(in Km)", "Streets(in Km)", "Path Holes (in Binary)"])
    ##X = X.replace(["Brown", "Blue"], [1, 0])
    
    # Get prediction
    prediction = clf.predict(X)[0]
    
    # Output prediction
    st.text(f"This instance is a {prediction}")

