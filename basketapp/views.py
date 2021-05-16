from django.shortcuts import HttpResponseRedirect, render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from mainapp.models import Course
from basketapp.models import Basket


@login_required
def basket_add(request, course_id=None):
    course = Course.objects.get(id=course_id)
    baskets = Basket.objects.filter(user=request.user, course=course)

    if not baskets.exists():
        Basket.objects.create(user=request.user, course=course, quantity=1)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_remove(request, id):
    Basket.objects.get(id=id).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_view(requests):
    basket = Basket.objects.filter(user=requests.user)
    context = {
        'title': 'GeekShop - Корзина',
        'baskets': basket,
    }
    return render(requests, 'basketapp/basket-view.html', context)


def basket_edit(request, id, quantity):
    if request.is_ajax():
        basket = Basket.objects.get(id=id)
        if quantity > 0:
            basket.quantity = quantity
            basket.save()
        else:
            basket.delete()
        baskets = Basket.objects.filter(user=request.user)
        context = {'baskets': baskets}
        result = render_to_string('basketapp/basket.html', context)
        return JsonResponse({'result': result})
