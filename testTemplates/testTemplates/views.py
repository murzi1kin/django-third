from django.http import HttpResponse
from django.shortcuts import render

MENU = {"главная":"/", "каталог":"/catalog", "о сайте":"/about"}

def main_page(request):
    # menu = ["главная", "каталог", "о сайте"]
    title = "Главная страница"
    # dict = {"name": "Ivan", "age": 23}
    data = {'menu': MENU, "title": title}
    return render(request, "./index.html", context=data)

def catalog_page(request):
    title = "Каталог"
    data = {'menu': MENU, "title": title}
    return render(request, "./catalog.html", context=data)

def about_page(request):
    title = "о компании"
    data = {'menu': MENU, "title": title}
    return render(request, "./about.html", context=data)