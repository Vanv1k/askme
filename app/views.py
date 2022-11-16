from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator
from . import models

# Create your views here.

def index(request, page:int = 1):
    paginator = Paginator(models.QUESTIONS, 5)
    page = request.GET.get('page')
    context = {"questions": paginator.get_page(page)}
    return render(request, 'index.html', context = context)

def question(request, id:int, page:int = 1):
    paginator = Paginator(models.ANSWERS, 4)
    page = request.GET.get('page')
    question_item = models.QUESTIONS[id]
    context = {'question': question_item, 'questions': paginator.get_page(page), 'answers': paginator.get_page(page)}
    return render(request, 'question.html', context = context)

def tag(request, tag_name:str, page:int = 1):
    question_list = []
    for i in models.QUESTIONS:
        if tag_name in i['tags']:
            question_list.append(i)
    paginator = Paginator(question_list, 5)
    page = request.GET.get('page')    
    context = {'questions': paginator.get_page(page), 'tag': tag_name}
    return render(request, 'tag.html', context = context)

def ask(request):
    return render(request, 'ask.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def settings(request):
    return render(request, 'settings.html')

