# flaskwithreact
flask for back-end it is  a project for nanodegree programe udacity
#api documention
1-endpoint="/questions"

  *method="get" parameter=page <int> =>return "dictonary {"questions":list of dictonary of questions data his length must be 10 or less,"total_questions": number of all quetions,"category": dictonary {"id of the category": type"}
  example of retrun 
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
                
  *method="post" data-posted{question: string,answer: string,difficulty: intger,category:intger=>return{"ok":"great"}
  
  
  2-endpoint=/questionssearch
  *method=post data-posted{searTerm: string} => return {"questions":like first endpoint but send only the questions have the searchTerm,"total_questions":like first endpoint}
  
  
  3-endpoint=/categories/<id>/questions
  id=intger the id of category
  *method=get=> return like the second endpoint but the qutions show only the questions with the same category id 
  4-endpoint=/questions/<id>
  id=inger the id of question
  *method=DELETE => return "ok"
  
  5- endpoint=/quizzes
  *method=POST date-posted{quiz_category:dictionary {"id": id of category, "type": type of category}=> return one question then return the next question in the next post when question finish will return the first question
  6-endpoint=/categories
  *method=GET => return the dictonary of category like the first endpoint
  
