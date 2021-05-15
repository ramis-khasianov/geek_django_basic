from django.shortcuts import HttpResponseRedirect, render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
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
    basket_count = 0
    basket_sum = 0
    for item in basket:
        basket_count += item.quantity
        basket_sum += item.sum()
    context = {
        'title': 'GeekShop - Корзина',
        'baskets': basket,
        'basket_count': basket_count,
        'basket_sum': basket_sum
    }
    return render(requests, 'basket/basket-view.html', context)
