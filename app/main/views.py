from flask import render_template
from . import main
 
@main.route('/')
def index():
    name='The Rustic Life'


    return render_template('index.html', name=name)



