import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/about')
def about ():
        return render_template('about.html')
@app.route('/contact')
def contact ():
        return render_template('contact.html')        
@app.route('/faq')
def faq ():
        return render_template('faq.html')    

@app.route('/store')
def store ():
        return render_template('store.html')


app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))