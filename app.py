from typing import List

import numpy as np
from flask import Flask, request, jsonify, render_template,redirect,url_for
import pickle
from flask import session, redirect
from functools import wraps
import pymongo

app = Flask(__name__)
app.secret_key = b'\xcc^\x91\xea\x17-\xd0W\x03\xa7\xf8J0\xac8\xc5'
model = pickle.load(open('model.pkl', 'rb'))
regressor = pickle.load(open('regressor.pkl', 'rb'))
svclassifier = pickle.load(open('svclassifier.pkl', 'rb'))

fin=[]
bin=[]
tin=[]

list1=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1]
disease=['Fungal infection',
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

abc=[]

 # Database
client = pymongo.MongoClient('localhost', 27017)
db = client.user_login_system
dd = client.history
# Decorators
def login_required(f):
  @wraps(f)
  def wrap(*args, **kwargs):
    if 'logged_in' in session:
      return f(*args, **kwargs)
    else:
      return redirect('/')
  
  return wrap


# Routes
from user import routes

@app.route('/')
def home():
  return render_template('home.html')


@app.route('/dashboard/',methods=["POST","GET"])
@login_required
def dashboard():
    if(request.method=="GET"):

        return render_template('index.html')
    elif (request.method=="POST"):
        data = request.json
        print(data)


        inp=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0 ,0 ,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for j in [1,2,3,4]:
            inp[int(j)]=1

        prediction = model.predict([np.array(inp)])
        prediction2 = regressor.predict([np.array(inp)])
        prediction1 = svclassifier.predict([np.array(inp)])
        print(prediction, prediction1, prediction2)
        
    
app.run(debug=True)


@app.route('/server/', methods=["GET","POST"])
@login_required
def server():

    if(request.method=="POST"):
        data = request.json
        array=data['list']

        

        inp=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0 ,0 ,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for j in array:
                inp[int(j)-1]=1

        prediction = model.predict([np.array(inp)])
        prediction2 = regressor.predict([np.array(inp)])
        prediction1 = svclassifier.predict([np.array(inp)])
        print(prediction, prediction1, prediction2)
        fin.append(disease[prediction[0]])
        bin.append(disease[prediction2[0]])
        tin.append(disease[prediction1[0]])
        
        paitent= {
        "email": {{ session['user']['email'] }},
        "symptoms":array,
        "diseases:":disease[prediction[0]]
        }
        curr = dd.paitent.find_one({ "email": paitent['email'] })
        if curr:
          dd.paitent.aggregate(paitent["symptoms"],paitent["diseases"])
        else:
          dd.paitent.insert_one(paitent)
        abc.append(disease[prediction[0]])

          

        
        return render_template('server.html',diss=fin)
    else:
        return render_template('server.html',diss=fin[-1],miss=bin[-1],tiss=tin[-1],noice=tin)


    




    