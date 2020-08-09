from flask import Flask
from flask import Blueprint,render_template
from .config import ProductionConfig

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html', URL = ProductionConfig.URL)

@main.route('/documentation')
def documentation():
    return render_template('documentation.html', URL = ProductionConfig.URL)