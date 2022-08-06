from importlib.resources import contents
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseNotFound, HttpResponseServerError

# Create your views here.
def home(request):
    return HttpResponse(content="Home page.")

def gallery(request):
    return HttpResponse(content=f"<h2>My gallery page.</h2>")

def archive(request, year: int):
    if request.GET:
        print(f'Your request include: \n{request.GET}')
    return HttpResponse(content=f"My gallery archive.<p>Year = {year}</p>")


def about(request):
    return HttpResponse(content="Hello, I'm Nikita, future web developer.")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found. Please ensure that the given data is valid.\nСторінка не знайдена. Будь ласка, перевірте чи є уведені дані вірними.</h1>')

def pageAccessDenied(request, exception):
    return HttpResponseNotAllowed('<h1>Highly sensetive information you\'ve not access to get.\nДуже вразлива інформація, на яку у Вас немає доступу.</h1>')

def pageServerError(request):
    return HttpResponseServerError('<h1>Server Error. We\'re working on it. Sorry for inconvinience.\nПомилка серверу. Ми працюємо над цим. Вибачте за незручності.</h1>')