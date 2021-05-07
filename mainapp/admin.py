from django.contrib import admin
from mainapp.models import CourseCategory, Course


admin.site.register(Course)
admin.site.register(CourseCategory)
