import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random
import json
from models import setup_db, Question, Category,db

QUESTIONS_PER_PAGE = 10


app = Flask(__name__)
# create and configure the app
cors=CORS(app)
setup_db(app)



@app.route("/questions",methods=["GET"])
def questions_get():
  pagenum=dict(request.args)["page"]
  questions=[]
  categores={}
  for q in list(db.session.query(Question).all()):
    questions.append({"id":q.id,
                      "question":q.question,
                      "answer":q.answer,
                      "category":q.category,
                      "difficulty":q.difficulty})  
  for c in db.session.query(Category).all():
    categores[c.id]=c.type
  total_questions=len(questions)
  startindex=int(pagenum)*10-10
  if total_questions//10< int(pagenum):
    questions=questions[startindex:]
  else:
    questions=questions[startindex:startindex+10]
  return {"questions":questions,
           "total_questions":total_questions,
           "categories":categores}



@app.route("/questions",methods=["POST"])
def questions_post():
    data=json.loads(request.data)
    question=Question(data["question"],data["answer"],data["difficulty"],data["category"])
    question.insert()
    return {"ok":"great"}

@app.route("/questionssearch",methods=["POST"])
def questions_search():
    data=json.loads(request.data)
    data=data["searchTerm"]
    print(data)
    questions=[]
    for q in list(db.session.query(Question).all()):
      if data.lower() in q.question.lower():
        questions.append({"id":q.id,
                      "question":q.question,
                      "answer":q.answer,
                      "category":q.category,
                      "difficulty":q.difficulty})
    return {"questions":questions,
             "total_questions":len(questions)}

@app.route("/categories")
def categories():
  categores={}
  for c in db.session.query(Category).all():
    categores[c.id]=c.type
  return {"categories":categores}
x=0
@app.route("/quizzes",methods=["POST"])
def quizzes():
    global x
    data=json.loads(request.data)
    print(data)
    list_id=[q.id for q in list(db.session.query(Question).filter_by(category=data["quiz_category"]["id"]).all())]
    print(list_id)
    if x>=len(list_id):
      x=0
    questions_id=list_id[x]
    
    
    q=db.session.query(Question).filter_by(id=questions_id).one()
    print(q)
    x+=1
    return {"question":{"id":q.id,
                      "question":q.question,
                      "answer":q.answer,
                      "category":q.category,
                      "difficulty":q.difficulty},
            "total":len(list_id)-1}

@app.route("/categories/<id>/questions")
def catgerory_questions(id):
  questions=[]
  for q in db.session.query(Question).filter_by(category=id).all():
    questions.append({"id":q.id,
                      "question":q.question,
                      "answer":q.answer,
                      "category":q.category,
                      "difficulty":q.difficulty})
  return {"questions":questions,
         "total_questions":len(questions)}

@app.route("/questions/<id>",methods=["DELETE"])
def questions_id(id):
    quetion=db.session.query(Question).filter_by(id=id).one().delete()
    return "ok"
@app.errorhandler(404)
def not_found_error(error):
    return {"error":"error 404"}
@app.errorhandler(402)
def not_found_error(error):
    return {"error":"error 402"}
@app.errorhandler(500)
def server_error(error):
    return {"error":"error 500"}
app.run()

    
