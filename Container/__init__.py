#!/usr/bin/env python3.7

import os
from flask import Flask, jsonify
from config import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from CustomExceptions import *
import secrets
import logging



app = Flask(__name__)
bcrypt = Bcrypt(app)

app.config.from_object(Config)

from models import db, Users,SessionManager

db.init_app(app)
migrate = Migrate(app, db)


@app.route('/api/create_new_session')
def create_new_session():
    logger = logging.getLogger(__name__)


    sessionID=secrets.token_hex(30)
    sessionID_hashed_b = str(bcrypt.generate_password_hash(sessionID).decode("utf-8"))
    
    
    
    session=SessionManager(session=sessionID_hashed_b)


    try:
        session.save()

    except Exception:
        logger.error("Error when trying to create new session.")
        return "Error when trying to create new session.", 500          

    resp = {
        "sessionID":sessionID
    }

    return jsonify(resp), 201



@app.route('/api/create_new_user/<username>/<password>')
def register(username,password):
    logger = logging.getLogger(__name__)

    password_hashed_b = str(bcrypt.generate_password_hash(password).decode("utf-8"))
    user = Users(username=username, password=password_hashed_b)

    try:
        
        user.save()

    except UserExistsError:
        logger.error("Error - User exists.")

        return "User exists", 400

    except Exception as e:
        logger.error("Error when trying to write data to the database")
        return f"Dabatase error {e}", 500

    resp = {
        'user:': username
    }

    return jsonify(resp), 201


if __name__ == '__main__':
    app.run(debug=True)