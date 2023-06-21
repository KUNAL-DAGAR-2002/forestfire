from flask import Flask,request,render_template
import pandas as pd
from sklearn.preprocessing import StandardScaler
import pickle as pkl

app = Flask(__name__)

scaler = pkl.load(open('models/scaler.pkl','rb'))
ridge = pkl.load(open('models/ridge.pkl','rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method=='POST':
        Temperature = float(request.form.get('Temperature'))
        RH = float(request.form.get('RH'))
        Ws = float(request.form.get('Ws'))
        Rain = float(request.form.get('Rain'))
        FFMC = float(request.form.get('FFMC'))
        DMC = float(request.form.get('DMC'))
        # ///////////////////////////////////
        ISI = float(request.form.get('ISI'))
        Classes = float(request.form.get('Classes'))
        region = float(request.form.get('region'))
        
        data = scaler.transform([[Temperature,RH,Ws,Rain,FFMC,DMC,ISI,Classes,region]])
        result = ridge.predict(data)
        return render_template('index.html',result=result)
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)