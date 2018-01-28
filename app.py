from flask import Flask
import os
from flask import request
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.secret_key = os.environ.get('SECRET_KEY')
db = SQLAlchemy(app)

class MyForm(FlaskForm):
    date = StringField('date', validators=[DataRequired()])
    number = StringField('number', validators=[DataRequired()])
    description = StringField('description', validators=[DataRequired()])
    amount = StringField('amount', validators=[DataRequired()])
    cleared = StringField('cleared', validators=[DataRequired()])


from models import Checkbook

@app.route('/testing')
def webhook():
    description = "ram"
    amount = "ramramramram"
    u = Checkbook(description=description, amount=amount)
    db.session.add(u)
    db.session.commit()
    return "user created"


@app.route('/')
def home():
    return render_template('index.html')


# @app.route('/')
# def submit():
#     form = MyForm()
#     if form.validate_on_submit():
#         return redirect('/success')
#     return render_template('hello.html', form=form)


@app.route('/checkbook', methods=['GET', 'POST'])
def checkbook():
    form = MyForm()
    if request.method == 'POST':
        date = request.form['date']
        number = request.form['number']
        description = request.form['description']
        amount = request.form['amount']
        cleared = request.form['cleared']
        fieldnames = ['date', 'number', 'description', 'amount', 'cleared']
        
    # show the form, it wasn't submitted
    return render_template('checkbook.html', form=form)

@app.route('/save-comment', methods=['POST'])
def save_comment():
    # This is to make sure the HTTP method is POST and not any other
    if request.method == 'POST':
        # request.form is a dictionary that contains the form sent through
        # the HTTP request. This work by getting the name="xxx" attribute of
        # the html form field. So, if you want to get the name, your input
        # should be something like this: <input type="text" name="name" />.
        name = request.form['name']
        comment = request.form['comment']

        # This array is the fields your csv file has and in the following code
        # you'll see how it will be used. Change it to your actual csv's fields.
        fieldnames = ['name', 'comment']

        # We repeat the same step as the reading, but with "w" to indicate
        # the file is going to be written.
        with open('nameList.csv','w') as inFile:
            # DictWriter will help you write the file easily by treating the
            # csv as a python's class and will allow you to work with
            # dictionaries instead of having to add the csv manually.
            writer = csv.DictWriter(inFIle, fieldnames=fieldnames)

            # writerow() will write a row in your csv file
            writer.writerow({'name': name, 'comment': comment})

        # And you return a text or a template, but if you don't return anything
        # this code will never work.
        return 'Thanks for your input!'