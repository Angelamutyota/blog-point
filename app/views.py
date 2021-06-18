from app.request import get_quotes
import re
from flask import render_template
from app import app

#views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    quotes = get_quotes()
    return render_template('index.html', quotes= quotes)
   