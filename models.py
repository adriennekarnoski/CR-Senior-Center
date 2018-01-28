from manage import db, app

class Checkbook(db.Model):
    __tablename__ = 'checkbook'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(30), index=True)
    number = db.Column(db.Integer, index=True)
    description = db.Column(db.String(64), index=True)
    amount = db.Column(db.Float, index=True)
    cleared = db.Column(db.String(30), index=True)

class CheckbookTotals(db.Model):
    __tablename__ = 'checkbook_totals'

    id = db.Column(db.Integer, primary_key=True)
    total_balance = db.Column(db.Float, index=True)
    total_cleared = db.Column(db.Float, index=True)
    number_cleared = db.Column(db.Integer, index=True)
    number_transactions = db.Column(db.Integer, index=True)