from flask import Flask, redirect, url_for, request, render_template
import os
from flask_sqlalchemy import SQLAlchemy

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SelectField
from wtforms.validators import DataRequired
from sqlalchemy import desc

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.secret_key = os.environ.get('SECRET_KEY')
db = SQLAlchemy(app)

class MyForm(FlaskForm):
    date = StringField('date', validators=[DataRequired()])
    number = IntegerField('number', validators=[DataRequired()])
    description = StringField('description', validators=[DataRequired()])
    amount = FloatField('amount', validators=[DataRequired()])
    cleared = SelectField('cleared', choices=[('YES', 'Yes'), ('NO', 'No')])
    cleared_date = StringField('cleared_date', validators=[DataRequired()])


from models import Checkbook


@app.route('/')
def home():
    return render_template('index.html')


# @app.route('/')
# def submit():
#     form = MyForm()
#     if form.validate_on_submit():
#         return redirect('/success')
#     return render_template('hello.html', form=form)


@app.route('/checkbook', methods=['GET'])
@app.route('/checkbook/<int:transaction_id>', methods=['GET', 'POST'])
def checkbook(transaction_id=None):
    new_form = MyForm()
    form = MyForm()
    if transaction_id:
        edit_post = db.session.query(Checkbook).get(transaction_id)
        form = MyForm(obj=edit_post)
    transactions = False
    if len(Checkbook.query.all()) != 0:
        transactions = True
        records = Checkbook.query.order_by(desc(Checkbook.id)).all()
        start = records[0].total
        book_total = records[0]
    else:
        records = None
        start = None
        book_total = None
    if request.method == 'POST':
        if request.path.split('/')[-1].isdigit():   
            return render_template(
                'checkbook.html',
                digit='yes',
                form=form,
                new_form=new_form,
                records=records,
                book_total=book_total)
    return render_template(
            'checkbook.html',
            digit=request.path.split('/')[-1],
            form=form,
            new_form=new_form,
            records=records,
            book_total=book_total)

@app.route('/checkbook/add', methods=['GET', 'POST'])
def add():
    form = MyForm()
    if request.method == 'POST':
        transactions = False
        if len(Checkbook.query.all()) != 0:
            transactions = True
            records = Checkbook.query.order_by(desc(Checkbook.id)).all()
            start = records[0].total
        date = request.form['date']
        number = request.form['number']
        description = request.form['description']
        amount = request.form['amount']
        cleared = request.form['cleared']
        if cleared == 'YES':
            cleared = True
            cleared_date = request.form['cleared_date']
        else:
            cleared = False
            cleared_date = 'Pending'
        if transactions:
            total = start + float(amount)
        else:
            total = amount
        fieldnames = [
            'date',
            'number',
            'description',
            'amount',
            'cleared',
            'cleared_date',
            ]
        c = Checkbook(
            date=date,
            number=number,
            description=description,
            amount=amount,
            cleared=cleared,
            cleared_date=cleared_date,
            total=total,
            )
        db.session.add(c)
        db.session.commit()
        if request.form['submit'] == 'Done':
            return redirect(url_for('checkbook'))
        if request.form['submit'] == 'Add Another':
            return redirect(url_for('add'))   
    return render_template('hello.html', form=form)


@app.route('/update/<int:transaction_id>')
def update(transaction_id):
    transaction = db.session.query(Checkbook).get(transaction_id)
    form = MyForm(obj=transaction)
    return render_template('hello.html', form=form)


@app.route('/delete')
def delete():
    db.session.query(Checkbook).delete()
    db.session.commit()
    return 'deleted'