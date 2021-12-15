from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST, require_GET, require_http_methods
from .models import FunnyWord


@require_GET
def index(request):
    words = serializers.serialize('json', FunnyWord.objects.all())
    return HttpResponse(words, content_type='application/json')
