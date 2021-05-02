from django.shortcuts import render
from mainapp.models import Course, CourseCategory


def index(requests):
    context = {'title': 'Geekshop'}
    return render(requests, 'mainapp/index.html', context)


def courses(requests):
    context = {
        'title': 'GeekShop - Каталог',
        'courses': Course.objects.all(),
        'categories': CourseCategory.objects.all(),
    }
    return render(requests, 'mainapp/courses.html', context)


def contacts(requests):
    context = {'title': 'Geekshop - Контакты'}
    return render(requests, 'mainapp/contacts.html', context)
