from django.db import models

# Create your models here.

QUESTIONS = [
    {
        'id': i,
        'title': 'title' + str(i),
        'text': 'text' + str(i),
        'numOfAnswers': i + i * 3,
        'tags' : ['tag' + str(i), 'tag' + str(i + 1), 'tag' + str(i + 2)],
        'likes': i*2 + i * 5,
    } for i in range(40)
]

ANSWERS = [
    {
        'id': i,
        'title': 'title' + str(i),
        'text': 'text' + str(i),
        'likes': i*2 + i * 5,
    } for i in range(10)
]