from module1 import db, app


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50),nullable=False)
    password = db.Column(db.String(100), nullable=False)


class UserReceipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    receipe_name = db.Column(db.String(10))
    receipe_des = db.Column(db.String(100))




with app.app_context():
    db.create_all()