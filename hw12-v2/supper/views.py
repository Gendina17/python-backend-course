from django.core import serializers
from django.core.exceptions import ValidationError
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST, require_GET
from .models import FunnyWord


@require_GET
def index(request):
    words = serializers.serialize('json', FunnyWord.objects.all())
    return HttpResponse(words, content_type='application/json')


@require_POST
def create(request):
    params = {key: value for key, value in request.POST.items()}
    try:
        word = FunnyWord.objects.create(**params)
        return HttpResponse(serializers.serialize('json', [word]), content_type='application/json')
    except ValidationError:
        return JsonResponse({'error': 'Произошла ошибка валидации данных'}, status=400)
