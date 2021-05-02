from django.db import models


class CourseCategory(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Course Categories'

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=256)
    image = models.ImageField(upload_to='course_images', blank=True)
    description = models.CharField(max_length=64, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.category.name} | {self.name}'
