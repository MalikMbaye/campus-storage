import os
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from wtforms import Form, StringField, DecimalField, TextAreaField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.secret_key = 'love'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/ubuntu/workspace/tmp/database.db'
db = SQLAlchemy(app)
class Moves(db.Model):
    __tablename__ = "Moves"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    location = db.Column(db.String(200))
    price = db.Column(db.Float(2))
    items = db.Column(db.Integer)

class MovesForm(Form):
        id = StringField('Name', validators=[DataRequired()])
        name = StringField('Name', validators=[DataRequired()])
        location = StringField('Name', validators=[DataRequired()])
        price = DecimalField('Name', validators=[DataRequired()])
        items = StringField('Name', validators=[DataRequired()])
        
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
@app.route('/history')
def history ():
        results = Moves.query.filter(1==1).all()
        return render_template('history.html', listings=results)
@app.route('/moves', methods=['GET','POST'])

def newmoves ():
        form = MovesForm(request.form)
        if request.method == 'POST':
                if form.validate() == False:
                        flash('All fields are required.')
                        return render_template('newmove.html', form=form)
                else:
                  lst = Moves(id=form.id.data, name=form.name.data, location=form.location.data, price=form.price.data, items=form.items.data )
                  db.session.add(lst)
                  db.session.commit()
                  results = Moves.query.filter(1==1).all()
                  return render_template('history.html', listings=results)  
        else:
                return render_template('newmove.html',form=form)
        

app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
