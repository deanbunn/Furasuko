from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Dean'}
    return render_template('index.html', title='Furasuko', user=user)




