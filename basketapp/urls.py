from django.urls import path

from basketapp.views import basket_add, basket_remove, basket_view, basket_edit

app_name = 'basketapp'

urlpatterns = [
    path('add/<int:course_id>/', basket_add, name='basket_add'),
    path('remove/<int:id>/', basket_remove, name='basket_remove'),
    path('basket-view', basket_view, name='basket_view'),
    path('edit/<int:id>/<int:quantity>/', basket_edit, name='basket_edit'),
]