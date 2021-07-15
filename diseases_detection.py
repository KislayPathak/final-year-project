# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 14:39:09 2021

@author: Kislay
"""
from sklearn.metrics import accuracy_score
import pickle
import pandas as pd
import matplotlib.pyplot as plt

setd=  pd.read_csv('D:/data/new_file.csv',skip_blank_lines=True, na_filter=True)
x=setd.iloc[:,1:-1].values
y=setd.iloc[:,0].values
diseases=['Fungal infection',
 'Allergy',
 'GERD',
 'Chronic cholestasis',
 'Drug Reaction',
 'Peptic ulcer diseae',
 'AIDS',
 'Diabetes ',
 'Gastroenteritis',
 'Bronchial Asthma',
 'Hypertension ',
 'Migraine',
 'Cervical spondylosis',
 'Paralysis (brain hemorrhage)',
 'Jaundice',
 'Malaria',
 'Chicken pox',
 'Dengue',
 'Typhoid',
 'hepatitis A',
 'Hepatitis B',
 'Hepatitis C',
 'Hepatitis D',
 'Hepatitis E',
 'Alcoholic hepatitis',
 'Tuberculosis',
 'Common Cold',
 'Pneumonia',
 'Dimorphic hemmorhoids(piles)',
 'Heart attack',
 'Varicose veins',
 'Hypothyroidism',
 'Hyperthyroidism',
 'Hypoglycemia',
 'Osteoarthristis',
 'Arthritis',
 '(vertigo) Paroymsal  Positional Vertigo',
 'Acne',
 'Urinary tract infection',
 'Psoriasis',
 'Impetigo']

attributes=['itching',
 ' skin_rash',
 ' nodal_skin_eruptions',
 ' dischromic _patches',
 '',
 ' continuous_sneezing',
 ' shivering',
 ' chills',
 ' watering_from_eyes',
 ' stomach_pain',
 ' acidity',
 ' ulcers_on_tongue',
 ' vomiting',
 ' cough',
 ' chest_pain',
 ' yellowish_skin',
 ' nausea',
 ' loss_of_appetite',
 ' abdominal_pain',
 ' yellowing_of_eyes',
 ' burning_micturition',
 ' spotting_ urination',
 ' passage_of_gases',
 ' internal_itching',
 ' indigestion',
 ' muscle_wasting',
 ' patches_in_throat',
 ' high_fever',
 ' extra_marital_contacts',
 ' fatigue',
 ' weight_loss',
 ' restlessness',
 ' lethargy',
 ' irregular_sugar_level',
 ' blurred_and_distorted_vision',
 ' obesity',
 ' excessive_hunger',
 ' increased_appetite',
 ' polyuria',
 ' sunken_eyes',
 ' dehydration',
 ' diarrhoea',
 ' breathlessness',
 ' family_history',
 ' mucoid_sputum',
 ' headache',
 ' dizziness',
 ' loss_of_balance',
 ' lack_of_concentration',
 ' stiff_neck',
 ' depression',
 ' irritability',
 ' visual_disturbances',
 ' back_pain',
 ' weakness_in_limbs',
 ' neck_pain',
 ' weakness_of_one_body_side',
 ' altered_sensorium',
 ' dark_urine',
 ' sweating',
 ' muscle_pain',
 ' mild_fever',
 ' swelled_lymph_nodes',
 ' malaise',
 ' red_spots_over_body',
 ' joint_pain',
 ' pain_behind_the_eyes',
 ' constipation',
 ' toxic_look_(typhos)',
 ' belly_pain',
 ' yellow_urine',
 ' receiving_blood_transfusion',
 ' receiving_unsterile_injections',
 ' coma',
 ' stomach_bleeding',
 ' acute_liver_failure',
 ' swelling_of_stomach',
 ' distention_of_abdomen',
 ' history_of_alcohol_consumption',
 ' fluid_overload',
 ' phlegm',
 ' blood_in_sputum',
 ' throat_irritation',
 ' redness_of_eyes',
 ' sinus_pressure',
 ' runny_nose',
 ' congestion',
 ' loss_of_smell',
 ' fast_heart_rate',
 ' rusty_sputum',
 ' pain_during_bowel_movements',
 ' pain_in_anal_region',
 ' bloody_stool',
 ' irritation_in_anus',
 ' cramps',
 ' bruising',
 ' swollen_legs',
 ' swollen_blood_vessels',
 ' prominent_veins_on_calf',
 ' weight_gain',
 ' cold_hands_and_feets',
 ' mood_swings',
 ' puffy_face_and_eyes',
 ' enlarged_thyroid',
 ' brittle_nails',
 ' swollen_extremeties',
 ' abnormal_menstruation',
 ' muscle_weakness',
 ' anxiety',
 ' slurred_speech',
 ' palpitations',
 ' drying_and_tingling_lips',
 ' knee_pain',
 ' hip_joint_pain',
 ' swelling_joints',
 ' painful_walking',
 ' movement_stiffness',
 ' spinning_movements',
 ' unsteadiness',
 ' pus_filled_pimples',
 ' blackheads',
 ' scurring',
 ' bladder_discomfort',
 ' foul_smell_of urine',
 ' continuous_feel_of_urine',
 ' skin_peeling',
 ' silver_like_dusting',
 ' small_dents_in_nails',
 ' inflammatory_nails',
 ' blister',
 ' red_sore_around_nose',
 ' yellow_crust_ooze']
#trainn test split
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
X_train,X_test,Y_train,Y_test=train_test_split(x,y,test_size=0.2)

from sklearn.naive_bayes import GaussianNB

#Create a Gaussian Classifier
model = GaussianNB()

# Train the model using the training sets
model.fit(x_train,y_train)
#pickle.dump(model, open('model.pkl','wb'))
y_pred= model.predict(x_test)# 0:Overcast, 2:Mild

#lR
from sklearn.linear_model import LogisticRegression
regressor=LogisticRegression()
regressor.fit(x_train,y_train)
#pickle.dump(regressor, open('regressor.pkl','wb'))
Y_pred=regressor.predict(x_test)

#svm
from sklearn.svm import SVC
svclassifier = SVC(kernel='linear')
svclassifier.fit(x_train, y_train)
#pickle.dump(svclassifier, open('svclassifier.pkl','wb'))
y_predsvm = svclassifier.predict(x_test)
x=[[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

accN=accuracy_score(y_test, y_pred)             #accuracy score Gausian naive bayes
bccN=accuracy_score(y_test, y_predsvm)          #accuracy score Svm
cccN=accuracy_score(y_test, Y_pred)             #accuracy score logistic regression

from sklearn.metrics import confusion_matrix
res = confusion_matrix(y_test,y_pred)
ves = confusion_matrix(y_test,Y_pred)
des = confusion_matrix(y_test,y_predsvm)
lol = svclassifier.predict(x)
print("logistic regression")
print(cccN*100)#
print("SVM")
print( bccN*100)#
print("Naive Bayes")
print(accN*100)#


plt.plot(x_train,y_train)
#plt.plot(x_test,y_predsvm)
#plt.plot(x_test,Y_pred)

plt.show()