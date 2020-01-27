"""The User part"""

from flask_sqlalchemy import SQLAlchemy
from CustomExceptions import *
from flask_session import Session

db = SQLAlchemy()

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(256))


    def save(self):

        try:

            query_result = Users.query.filter_by(username=self.username).first()

        except Exception as e:

            # raise DatabaseError(f"Database error {e}") 
            raise e

        if query_result:
                           
            raise UserExistsError("User already exists")

        elif query_result is None:

            db.session.add(self)
            db.session.commit()
              


"""Session management"""

class SessionManager(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    session = db.Column(db.String(200))

    def save(self):

        try:
            db.session.add(self)
            db.session.commit()

        except Exception:
            raise DatabaseError("There an issue with the Database.")
        
