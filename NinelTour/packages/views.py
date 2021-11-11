import json
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST, require_GET, require_http_methods
from packages.models import Package
from django.core.exceptions import ValidationError


@require_GET
def index(request):
    packages = serializers.serialize('json', Package.objects.all())
    return HttpResponse(packages, content_type='application/json')


@require_GET
def show(request, departure_country):
    packages = serializers.serialize('json', Package.objects.filter(departure_country=departure_country))
    if len(packages) == 2:
        return JsonResponse({'error': 'Не найдено ни одного туристического пакета'}, status=404)
    return HttpResponse(packages, content_type='application/json')


@require_POST
def create(request):
    params = {key: value for key, value in request.POST.items()}
    try:
        package = Package.objects.create(**params)
        return HttpResponse(serializers.serialize('json', package), content_type='application/json')
    except ValidationError:
        return JsonResponse({'error': 'Произошла ошибка валидации данных'})


@require_http_methods(['PUT'])
def update(request, id):
    try:
        count = Package.objects.filter(id=id).update(**json.loads(request.body))
        if count == 0:
            return JsonResponse({'error': 'Не удалось обновить объект'})
        return JsonResponse({'message': f'Туристический пакет с id = {id} обновлен успешно'})
    except ValidationError:
        return JsonResponse({'error': 'Произошла ошибка валидации данных'})


@require_http_methods(['DELETE'])
def delete(request, id):
    code, data = Package.objects.filter(id=id).delete()
    if code == 0:
        return JsonResponse({'error': f'Пакет с id = {id} не найден'}, status=404)
    return JsonResponse({'message': f'Пакет с  id = {id} удален'})

