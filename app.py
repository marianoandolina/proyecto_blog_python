from flask import Flask, render_template, jsonify, request

import traceback
import os
import csv
import sqlite3


import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship


app = Flask(__name__)
engine = sqlalchemy.create_engine("sqlite:///blog.db")
base = declarative_base()

@app.before_first_request
def before_first_request_func():
    # Crear aquí todas las bases de datos

    class Post(base):
        __tablename__ = 'post'

        id = Column(Integer, primary_key=True)
        username = Column(String)
        titulo = Column(String)
        texto = Column(String)

    base.metadata.create_all(engine)
    print("Base de datos generada")


@app.route("/")
def index():
    try:
        return render_template('blog.html')
    except:
        return jsonify({'trace': traceback.format_exc()})


@app.route("/login")
def login():
    try:
        return render_template('login.html')
    except:
        return jsonify({'trace': traceback.format_exc()})

@app.route("/post", methods = ['GET', 'POST'])
def post():
    if request.methods == ['GET']:
        try:
            username = str(request.args.get('username'))
            print(username)
        except:
            return jsonify({'trace': traceback.format_exc()})



    


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)

