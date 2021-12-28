# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 23:27:57 2021

@author: henry
"""
# install eel


import eel
import pandas as pd
import numpy as np
import requests
from flask import Flask, render_template, request

eel.init('web')


@eel.expose
def recommendation(num1): 
  #response = requests.get("http://localhost:8000/sum")
  response = requests.post("http://localhost:8000/Recommendation", data ={'input':num1})
  print(response)
  return response.json()


@eel.expose
def get_data(inp):
    data = pd.read_excel('./CategoryNamesList.xlsx', sheet_name='CategoryNamesList')
    #data = pd.read_csv('D:/ISM/structureValidatingProcedures/Task3DataSet/Strukturbaum_Namen.csv',encoding='cp1252', dtype='unicode')
                       
    df = pd.DataFrame(data, columns= ['category_en','category_id'])
    return  (df.to_json())


#@app.route("/home")
#def home():
#    suggestions = get_suggestions()
#    return render_template('home.html',suggestions=suggestions)

eel.start('index.html', mode='edge')

