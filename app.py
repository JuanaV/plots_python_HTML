# -*- coding: utf-8 -*-

# Create an application with Python and Flask to create and update data


from flask import Flask, jsonify, render_template, request
import numpy as np 
import base64
app = Flask(__name__)

@app.route('/_update')
def update():
    # Edit here the data you want to plot and update
    linesData = np.random.rand(10,2).tolist()
    barData = list(np.random.rand(1,2)[0])
    radarData = list(np.random.rand(1,8)[0])
    
    
    return jsonify(linesData=linesData, barData=barData, radarData=radarData)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()