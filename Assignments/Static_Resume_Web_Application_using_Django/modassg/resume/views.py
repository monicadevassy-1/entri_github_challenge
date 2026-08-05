from django.http import HttpResponse
from django.shortcuts import render

Profile=[{"name": "Monica Devassy",
          "age":"28",
          "gender":"Female",
          "phone":"+91-8281658699",
        "email": "monicadevassy@gmail.com",
        "linkedin":"https://www.linkedin.com/in/monica-devassy",
        "github":" https://github.com/monicadevassy-1",
        "summary":"Aspiring Python Developer with training in Python, Django, REST API, "
        "and AI technologies, along with knowledge of backend and web application development. Skilled in Python programming, OOP concepts, MySQL/SQLite, Django ORM, CRUD operations, authentication, Celery, Redis, GitHub, and deployment. Familiar with HTML, CSS, JavaScript, and committed to building scalable and efficient software solutions. ",
        "skills":"Python | Django | HTML | CSS | JavaScript",
        "education": {
            "degree": "B.Tech in Civil Engineering",
            "college": "Christ College of Engineering,Irinjalakuda,Thrissur",
            "year": "2015-19",},
        "experience":{
            "company":"Infosys Ltd",
            "desc":"Worked with middleware technologies including IBM WebSphere Application Server (WAS) and IBM MQ to support application communication and system performance. ",
            "location":"Chennai"},
        "cert":{"inst":"Entri Software Private Limited | Illinois Institute,Chicago |NSDC ",
        "prog":"Program in AI Driven Python Programming "}
            
        }]

def res(request):
    return render(request, 'myhtml.html', {'profile': Profile})
#for every new function update urls.py adn settings--template and installed apps1
