from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import OperatorAnalysis, RegulatorAnalysis
from werkzeug.urls import url_parse

@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html', title="Home Page")

@app.route('/operatorAnalysis', methods=['GET','POST'])
def operatorAnalysis():
    form = OperatorAnalysis()
    if form.validate_on_submit():
        return render_template('results.html', title="Results")
    return render_template('operatorAnalysis.html', title=" Regulator Analysis", form=form)

@app.route('/regulatorAnalysis', methods=['GET','POST'])
def regulatorAnalysis():
    form = RegulatorAnalysis()
    if form.validate_on_submit():
        return render_template('results.html', title="Results")
    return render_template('regulatorAnalysis.html', title="Regulator Analysis", form=form)

