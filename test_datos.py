#!/usr/bin/env python
# -*- coding: utf-8 -*-

from apptrivia import db
from models.models import Categoria, Pregunta

db.drop_all()
db.create_all()

# categorias
c_geogra = Categoria(descripcion="Geografía")
c_deporte = Categoria(descripcion="Deportes")

# preguntas
q_Laos = Pregunta(text="¿Cuál es la capital de Laos?", categoria = c_geogra)
q_Armenia = Pregunta(text="¿Cuál es la población aproximada de Armenia?", categoria = c_geogra)
q_mundial = Pregunta(text="¿En qué país se jugó la Copa del Mundo de 1962?", categoria = c_deporte)



db.session.add(c_geogra)
db.session.add(c_deporte)
db.session.add(q_Laos)
db.session.add(q_Armenia)
db.session.add(q_mundial)
db.session.commit()

# creamos otros usuarios (…) y los recorremos
categorias = Categoria.query.all()
for c in categorias:
    print(c.id, c.descripcion)
    # para cada categoria, obtenemos sus preguntas y las recorremos
    for p in c.preguntas:
        print(p.id, p.text)


cat = Categoria.query.get(1)
print(cat)

