## Projet d'apprentissage automatique de bout en bout - Prédiction de l'éligibilité aux prêts à l'aide de l'apprentissage automatique

<img target="_blank" src="./images/pret.jpg" width=600>

### Table des matières
  
  * [Vue d'ensemble](#vued'ensemble)
  * [Informations sur le jeu de données](#jeudedonnées)
  * [Motivation](#motivation)
  * [Démo](#démo)
  * [Étapes de l'exécution du projet](#Objectif d'apprentissage)
  * [Aspect technique](#aspect-technique)
  * [Technologies utilisées](#technologies-utilisées)
  * [Installation](#installation)
  * [Remarque](#note)


### Vue d'ensemble
Les bénéfices et les pertes d’une banque dépendent du montant des prêts, c’est-à-dire du fait que le client ou le consommateur rembourse le prêt. Le recouvrement des prêts est la tâche la plus fastidieuse du secteur bancaire.

La société King finance s’occupe de toutes sortes de prêts immobiliers. Elle est présente dans toutes les zones urbaines, semi-urbaines et rurales. Le client demande d’abord un prêt immobilier, puis l’entreprise valide l’éligibilité du client au prêt.

L’entreprise souhaite automatiser le processus d’éligibilité au prêt (en temps réel) en fonction des informations fournies par le client lors du remplissage des formulaires de demande en ligne. Ces informations sont le sexe, l’état matrimonial, l’éducation, le nombre de personnes à charge, le revenu, le montant du prêt, l’historique de crédit, etc.

Pour automatiser ce processus, ils ont fourni un ensemble de données permettant d’identifier les segments de clientèle éligibles aux montants des prêts afin de pouvoir cibler spécifiquement ces clients.

Les données historiques des candidats ont été utilisées pour construire un modèle d’apprentissage automatique utilisant différents algorithmes de classification. L’objectif principal de ce projet est de prédire si un nouveau demandeur a accordé le prêt ou non à l’aide de modèles d’apprentissage automatique formés sur l’ensemble de données historiques.

Dans ce projet, nous allons appliquer des techniques de machine learning et développer une application Web pour prédire l'éligibilité au prêt d'un nouveau demandeur.

### Informations sur le jeu de données

Variable	          Description

Loan_ID	            ID de prêt unique

Gender	            Sexe Homme/ Femme

Married	            Marié Demandeur marié (O/N)

Dependents	        Nombre de personnes à charge

Education	         Éducation du demandeur (Diplôme/Premier cycle)

Self_Employed	      Auto emploi (O/N)

ApplicantIncome	    Revenu du demandeur

CoapplicantIncome	  Revenu du co-demandeur

LoanAmount	        Montant du prêt


Loan_Amount_Term	  Durée du prêt en mois

Credit_History	    Historique de crédit

Property_Area	      Urbain/ Semi Urbain/ Rural

Loan_Status	        Prêt accordé (O/N)


jeu de données final: 615 observations

L'ensemble de données utilisé dans ce projet peut être trouvé ici : [Dataset] https://www.kaggle.com/datasets/ninzaami/loan-predication


### Motivation

L'objectif était d'utiliser des expériences d'apprentissage automatique pour essayer d'automatiser le processus d'éligibilité au prêt avec un faible risque et un meilleur recouvrement.



### Démo


Application Web Snapshot:

<img target="_blank" src="./images/Capture.PNG" width=800>



### Étapes de l'exécution du projet

- Collecte de données 
- Analyse descriptive 
- Visualisations de données 
- Prétraitement des données 
- Modélisation des données 
- Évaluation du modèle 
- Déploiement du modèle 

### Aspect technique 

- Entraînement d'un modèle d'apprentissage automatique à l'aide de scikit-learn. 
- Création et hébergement d'une application Web streamlit sur Heroku. 
- Un utilisateur doit entrer les informations clés.
- Une fois qu'il obtient toutes les informations des champs, la prédiction est affichée. 


### Technologies utilisées  
![](https://forthebadge.com/images/badges/made-with-python.svg) 

<img target="_blank" src="https://github.com/dipakml/Prediction-of-Concrete-Compressive-Strength/blob/master/Logo_Images/streamlit.png" width=160>
<img target="_blank" src="https://github.com/dipakml/Prediction-of-Concrete-Compressive-Strength/blob/master/Logo_Images/numpy.png" width=160>
<img target="_blank" src="https://github.com/dipakml/Prediction-of-Concrete-Compressive-Strength/blob/master/Logo_Images/pandas.jpeg" width=160>

### Installation 
- Clonez ce dépôt et décompressez-le.
- Après le téléchargement, cd dans le répertoire de travail.
- Commencez un nouveau environnement virtuel avec Python 3 et activez-le.
- Installez les packages requis en utilisant pip install -r requirements.txt
- Exécutez la commande: streamlit run app.py


### Remarque:
- L'application Web peut gérer la concurrence jusqu'à un certain niveau mais peut être mise à l'échelle.

