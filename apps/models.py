from apps import db

class Member(db.Model):
    __tablename__ = 'member'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    province_id = db.Column(db.Integer)
    city_id = db.Column(db.Integer)
    add_time = db.Column(db.Integer)

    def __repr__(self):
        return '<Member %r>' % self.username

