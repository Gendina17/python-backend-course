from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST, require_GET, require_http_methods
import json
from django.core import serializers
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from users.models import User

FIELDS = ("first_name", "last_name", "email", "birthday", "gender", "passport_number", "phone")


@require_GET
def index(request):
    users = serializers.serialize('json', User.objects.all(), fields=FIELDS)
    return HttpResponse(users, content_type='application/json')


@require_GET
def show(request, id):
    user = get_object_or_404(User, id=id)
    return HttpResponse(serializers.serialize('json', [user], fields=FIELDS), content_type='application/json')


@require_POST
def create(request):
    params = {key: value for key, value in request.POST.items()}
    try:
        user = User.objects.create(**params)
        return HttpResponse(serializers.serialize('json', User.objects.filter(id=user.id)),
                            content_type='application/json')
    except ValidationError:
        return JsonResponse({'error': 'Произошла ошибка валидации данных'}, status=400)


@require_http_methods(['PUT'])
def update(request, id):
    try:
        count = User.objects.filter(id=id).update(**json.loads(request.body))
        if count == 0:
            return JsonResponse({'error': 'Не удалось обновить клиента'}, status=400)
        return JsonResponse({'message': f'Клиент с id = {id} обновлен успешно'})
    except ValidationError:
        return JsonResponse({'error': 'Произошла ошибка валидации данных'}, status=400)


@require_http_methods(['DELETE'])
def delete(request, id):
    code, data = User.objects.filter(id=id).delete()
    if code == 0:
        return JsonResponse({'error': f'Клиент с id = {id} не найден'}, status=404)
    return JsonResponse({'message': f'Клиент с  id = {id} удален'})
