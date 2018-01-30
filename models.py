from manage import db, app


class Checkbook(db.Model):
    __tablename__ = 'checkbook'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(30))
    number = db.Column(db.Integer)
    description = db.Column(db.String(64))
    amount = db.Column(db.Float)
    cleared = db.Column(db.Boolean, default=False)
    cleared_date = db.Column(db.String(30))
    total = db.Column(db.Float)

