import json
from flask import Flask, render_template, request, url_for, redirect
app = Flask(__name__)

@app.route('/')
def proba7():
    urls = {'главная страница с анкетой': url_for('proba7'),
            'Статистика': url_for('stats'),
            'Все данные': url_for('json'),
            'Поиск': url_for('search'),
            'Результаты': url_for('results')}
    return render_template('proba7.html', urls=urls)
            
            


@app.route('/json')
def json():
    








@app.route('/stats',)

@app.route('/search',)
    
    

 
