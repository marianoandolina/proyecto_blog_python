from flask import Flask, render_template, jsonify, request

import traceback
import os
import csv
import sqlite3


import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, session


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
    if request.method == ['GET']:
        try:            
            user = str(request.args.get('username'))

            Session = sessionmaker(bind=engine)
            session = Session

            posts = []      
            query = session.query(Post).filter(post.name == user)
            all_post = query.all().order_by(Post.id.desc().limit(2))

            for post in all_post:
                post.append(post)

            return jsonify({"posts": posts})
    
                 
        except:
            return jsonify({'trace': traceback.format_exc()})
        
    if request.method == ['POST']:
        try:
            username = request.form('username')
            titulo = request.form('titulo')
            texto = request.form('texto')

            Session = sessionmaker(bind=engine)
            session = Session()
            
            post = Post(username=username, titulo=titulo, texto=texto)

            session.add(post)
            session.commit()
        
        except:
            return jsonify({'trace': traceback.format_exc()})




    


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)

