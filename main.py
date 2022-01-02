# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 23:27:57 2021

@author: henry
"""
# install eel

from bottle import redirect, template
import pandas as pd
import numpy as np
import requests
from flask import Flask, render_template, request, jsonify

app= Flask(__name__) #, template_folder='web')

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/recommendation', methods=['GET'])
def recommendation(): 
  paras={"input": request.args.get('inp')}
  #response = requests.get("http://localhost:8000/sum")
  response = requests.post("https://rmodel-recommendation.herokuapp.com/analyse", params= paras)
  return response.json()


#@eel.expose
@app.route('/getExcelData', methods=['GET'])
def get_data():
    data = pd.read_excel('./CategoryNamesList.xlsx', sheet_name='CategoryNamesList')
    #data = pd.read_csv('D:/ISM/structureValidatingProcedures/Task3DataSet/Strukturbaum_Namen.csv',encoding='cp1252', dtype='unicode')
                       
    df = pd.DataFrame(data, columns= ['category_en','category_id'])
    return  (df.to_json())

if __name__ == '__main__':
  app.debug = True
  app.run()
