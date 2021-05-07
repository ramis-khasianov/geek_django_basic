from django.urls import path

from mainapp.views import courses

app_name = 'mainapp'

urlpatterns = [
    path('', courses, name='index'),
    path('<int:id>/', courses, name='courses'),
]
