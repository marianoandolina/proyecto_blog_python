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

class Post(base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    titulo = Column(String)
    texto = Column(String)

@app.before_first_request
def before_first_request_func():
    # Crear aquí todas las bases de datos

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

@app.route("/post", methods=['GET', 'POST'])
def post():
    try:
        if request.method == 'GET':

            usuario = str(request.args.get('username'))
            print(f"El usuario ingresado es: {usuario}")
                  

            Session = sessionmaker(bind=engine)
            session = Session

            posts = []

            query = session.query(Post).filter(Post.name == usuario)
            print(query)
            
            all_post = query.all().order_by(Post.id.desc().limit(2))
            print(post)

            for post in all_post:
                posts.append(post)
        
            return jsonify({"posts": posts})

        if request.method == 'POST':

            usuario = str(request.args.get('username'))
            print(f'El usuario que escribio el post es: {usuario}')

            titulo = request.form['titulo']
            texto = request.form['texto']
            print(f"El usuario es {username}, el titulo es {titulo} y el texto es {texto}")

            Session = sessionmaker(bind=engine)
            session = Session()
            
            post = Post(username=username, titulo=titulo, texto=texto)

            session.add(post)
            session.commit()

            return jsonify({"id": post.id, "titulo": post.titulo, "texto": post.texto})    
            # return render_template('blog.html', mensaje='enviado')    
            
    except:
        return jsonify({'trace': traceback.format_exc()})

if __name__ == "__main__":

    app.run(host="127.0.0.1", port=5000, debug=True)
