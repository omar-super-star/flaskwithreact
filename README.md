# flaskwithreact
flask for back-end it is  a project for nanodegree programe udacity
#api documention



GET /categories

 fetches a dictonary of categories in which the keys are the ids and the value is the corresponding string of category
 
 request args= None
 
 returns: an object with a single key ,categores that contains of object id: category_string
 
 {"1": "science",
 "2":"arts",
 "3":"geography",
 "4":"history",
 "5":"entertainment",
 "6":"sports"}
 
GET questions?page=<int>
 
  fetches a list of questions(only 10) and dictonary categories and total answer(int) 
  
  return an opject key is "questions,total_questions,category"
  
  -example
  {"questions":[{"id":1,
               "question":"what is th gravity,
                "answer":is a power,
                "category":science,
                 "difficulty":1},
                {"id":2,
               "question":"what is the g,
                "answer":9.8,
                "category":science,
                 "difficulty":1}],
  
   "total_questions":2,
   "category":{"1":"science",
                "2":"art",}
                }
                
   POST questions
   
   add the data to the question table
   
   request aargs:question: string,answer: string,difficulty: intger,category:intger
   
   return{"ok":"great"}
  
  
   POST /questionssearch
   
    fetch the questions which  include the searchTerm in list 
    
   return dictonary his key is question and total_questions
   
   example:
   {"questions":[{"id":1,
               "question":"what is th gravity,
                "answer":is a power,
                "category":science,
                 "difficulty":1},
                {"id":2,
               "question":"what is the g,
                "answer":9.8,
                "category":science,
                 "difficulty":1}],
  
   "total_questions":2}
  
  
  
   GET endpoint=/categories/<id>/questions
 
    fetch the questions which  have the category id in list 
    
   request args: id=intger the id of category
   
   return  dictonary his key is question and total_questions
   
   example 
 {"questions":[{"id":1,
               "question":"what is th gravity,
                "answer":is a power,
                "category":science,
                 "difficulty":1},
                {"id":2,
               "question":"what is the g,
                "answer":9.8,
                "category":science,
                 "difficulty":1}],
  
   "total_questions":2}
   
   
  DELETE /questions/<id>
  
  id=inger the id of question
  
  delete the question have the id from the table of database
  example return "ok"
  
  POST endpoint=/quizzes
  request-data= dictonary {quiz_category:dictionary {"id": id of category, "type": type of category}
 
   return one question then return the next question in the next post when question finish will return the first question
   
   example 
   first time:
       {"id":1,
               "question":"what is th gravity,
                "answer":is a power,
                "category":science,
                 "difficulty":1}
  second time:
         {"id":2,
               "question":"what is the g,
                "answer":9.8,
                "category":science,
                 "difficulty":1}
  
  
 
  
