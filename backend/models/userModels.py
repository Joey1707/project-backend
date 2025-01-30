# from backend.app import db

# class User(db.Model):
#     __tablename__ = 'userData'

#     personID = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     username = db.Column(db.String(50), nullable=False)
#     age = db.Column(db.SmallInteger)
#     passwd = db.Column(db.String(50), nullable=False)
#     email = db.Column(db.String(100), nullable=False, unique=True)

#     def __repr__(self):
#         return f"<User {self.username}>"
