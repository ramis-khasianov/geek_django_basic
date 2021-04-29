from django.shortcuts import render
import os
import json


module_dir = os.path.dirname(__file__)


def index(requests):
    context = {'title': 'Geekshop'}
    return render(requests, 'mainapp/index.html', context)


def catalog(requests):
    json_file_path = os.path.join(module_dir, 'fixtures/courses.json')
    courses = json.load(open(json_file_path, encoding='utf8'))
    context = {
        'title': 'Geekshop - Каталог',
        'courses': courses
    }
    return render(requests, 'mainapp/catalog.html', context)


def contacts(requests):
    context = {'title': 'Geekshop - Контакты'}
    return render(requests, 'mainapp/contacts.html', context)
