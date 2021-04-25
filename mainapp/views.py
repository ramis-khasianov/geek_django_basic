from django.shortcuts import render


def index(requests):
    return render(requests, 'mainapp/index.html')


def catalog(requests):
    return render(requests, 'mainapp/catalog.html')


def contacts(requests):
    return render(requests, 'mainapp/contacts.html')
