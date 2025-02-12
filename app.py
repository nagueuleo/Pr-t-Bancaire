# -*- coding: utf-8 -*-


import numpy as np
import pickle
import pandas as pd
import streamlit as st 
import base64
from PIL import Image

pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)  
IMG_SIDEBAR_PATH = "./images/donner.jpg"

pickle_sc = open("sc.pkl","rb")
sc=pickle.load(pickle_sc)  

def get_base64(file_path):
    with open(file_path, "rb") as file:
        encoded_string = base64.b64encode(file.read()).decode()
    return f"data:image/jpg;base64,{encoded_string}"

def set_background(image_path):
    base64_image = get_base64(image_path)
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{base64_image}");
            background-attachment: fixed;
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Utilisation de la fonction avec ton image
set_background("images/bg.jpg")


def predict(Gender, Married, Education, Self_Employed, ApplicantIncome,
       CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History,
       Dependents_0, Dependents_1, Dependents_2,
       Property_Area_Semiurban, Property_Area_Urban):
   
    prediction=classifier.predict([[Gender, Married, Education, Self_Employed, ApplicantIncome,
       CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History,
       Dependents_0, Dependents_1, Dependents_2,
       Property_Area_Semiurban, Property_Area_Urban]])
    print(prediction)
    return prediction



def main():
    html_temp = """
    <div style="background-color:blue;padding:10px">
    <h3 style="color:white;text-align:center;">Prédiction de l'éligibilité au prêt à l'aide de l'apprentissage automatique</h3>
    </div>
    """
    st.sidebar.header("Données Personnelles du demandeur 💸")
    st.markdown(html_temp,unsafe_allow_html=True)
    image = np.array(Image.open(IMG_SIDEBAR_PATH))
    st.sidebar.image(image)


    st.markdown('**Application Web pour vérifier l\'éligibilité au prêt. Entrer les informations ci-dessous pour prédire l\'éligibilité au prêt.**')
    Gender = st.sidebar.selectbox("Genre",("Homme","Femme"))
    if Gender == 'Homme':
        Gender = 1
    else:
        Gender = 0

    Married = st.sidebar.selectbox("Marié",("Oui","Non"))
    if Married == 'Oui':
        Married = 1
    else:
        Married = 0

    Dependents = st.sidebar.selectbox("Personnes à charge",("0","1","2", "3"))
    if Dependents == '0':
        Dependents_0 = 1
        Dependents_1 = 0
        Dependents_2 = 0
    elif Dependents == '1':
        Dependents_0 = 0
        Dependents_1 = 1
        Dependents_2 = 0
    elif Dependents == '2':
        Dependents_0 = 0
        Dependents_1 = 0
        Dependents_2 = 1
    else:
        Dependents_0 = 0
        Dependents_1 = 0
        Dependents_2 = 0

    Education = st.sidebar.selectbox("Éducation",("Diplômé","Pas diplômé"))
    if Education == 'Diplômé':
        Education = 1
    else:
        Education = 0       

    Self_Employed = st.sidebar.selectbox("Auto emploi",("Oui","Non"))
    if Self_Employed == 'Oui':
        Self_Employed = 1
    else:
        Self_Employed = 0 



    ApplicantIncome = st.number_input("Indiquer le revenu du demandeur entre 150 et 80 000")

    CoapplicantIncome = st.number_input("Indiquer le revenu du Co-demandeur entre 0 et 40,000")

    LoanAmount = st.number_input("Entrez le montant du prêt entre 0 et 700")

    Loan_Amount_Term = st.number_input("Entrez le montant de la durée du pret entre 12 et 480")

    Credit_History = st.number_input("Entrez l'historique de crédit entre 0 ou 1")

    Property_Area = st.sidebar.selectbox("Superficie de la propriété", ("Urbain", "Rural", "Semi-urbain"))
    if Property_Area == 'Urbain':
        Property_Area_Urban = 1
        Property_Area_Semiurban = 0
    elif Property_Area == 'Semi-urbain':
        Property_Area_Urban = 0
        Property_Area_Semiurban = 1
    else:
        Property_Area_Urban = 0
        Property_Area_Semiurban = 1         


    
    result=""
    if st.button("Prédiction"):
        result=classifier.predict(sc.transform([[Gender, Married, Education, Self_Employed, ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History, Dependents_0, Dependents_1, Dependents_2, Property_Area_Semiurban, Property_Area_Urban]]))
        if result ==1:
            return st.header('Vous êtes éligible pour bénéficier du prêt')
        else:
            return st.header('Désolé, vous n\'êtes pas éligible pour bénéficier du prêt')
if __name__=='__main__':
    main()
    
    
    