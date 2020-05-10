# importamos la instancia de Flask (app)
from apptrivia import app
import random

# importamos los modelos a usar
from models.models import Categoria, Pregunta

from flask import render_template

@app.route('/trivia')
def index():
    return "<h2>hola Trivia</h2>"


@app.route('/trivia/categorias', methods=['GET'])
def mostrarcategorias():
    categorias = Categoria.query.all()
    return render_template('categorias.html', categorias=categorias)


@app.route('/trivia/<int:id_categoria>/pregunta', methods=['GET'])
def mostrarpregunta(id_categoria):
    preguntas = Pregunta.query.filter_by(categoria_id=id_categoria).all()
    # elegir pregunta aleatoria pero de la categoria adecuada
    pregunta = random.choice(preguntas)
    categ = Categoria.query.get(id_categoria)
    return render_template('preguntas.html', categoria=categ, pregunta=pregunta)
