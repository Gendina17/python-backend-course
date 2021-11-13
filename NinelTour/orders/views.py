from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST, require_GET, require_http_methods
from orders.models import Order
import json
from django.core import serializers
from django.core.exceptions import ValidationError


@require_GET
def index(request):
    orders = serializers.serialize('json', Order.objects.all())
    return HttpResponse(orders, content_type='application/json')


@require_GET
def show(request, user_id):
    orders = serializers.serialize('json', Order.objects.filter(user_id=user_id))
    if len(orders) == 2:
        return JsonResponse({'error': 'Не найдено ни одного заказа для данного пользователя'}, status=404)
    return HttpResponse(orders, content_type='application/json')


@require_POST
def create(request):
    params = {key: value for key, value in request.POST.items()}
    try:
        order = Order.objects.create(**params)
        return HttpResponse(serializers.serialize('json', order), content_type='application/json')
    except ValidationError:
        return JsonResponse({'error': 'Произошла ошибка валидации данных'}, status=400)


@require_http_methods(['PUT'])
def update(request, id):
    try:
        count = Order.objects.filter(id=id).update(**json.loads(request.body))
        if count == 0:
            return JsonResponse({'error': 'Не удалось обновить заказ'}, status=404)
        return JsonResponse({'message': f'Заказ с id = {id} обновлен успешно'})
    except ValidationError:
        return JsonResponse({'error': 'Произошла ошибка валидации данных'}, status=400)


@require_http_methods(['DELETE'])
def delete(request, id):
    code, data = Order.objects.filter(id=id).delete()
    if code == 0:
        return JsonResponse({'error': f'Заказ с id = {id} не найден'}, status=404)
    return JsonResponse({'message': f'Заказ с  id = {id} удален'})
