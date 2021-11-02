from django.http import JsonResponse

USERS = [{'id': 1, 'name': 'Нина', 'surname': 'Гендина', 'birthday': '17-06-2001', 'gender': 'ж'},
         {'id': 2, 'name': 'Роман', 'surname': 'Баканов', 'birthday': '26-05-2001', 'gender': 'м'},
         {'id': 3, 'name': 'Дмитрий', 'surname': 'Пудовкин', 'birthday': '04-11-2001', 'gender': 'м'},
         {'id': 4, 'name': 'Сергей', 'surname': 'Шишкин', 'birthday': '21-06-2001', 'gender': 'м'}]


def index(request):
    if request.method == 'GET':
        return JsonResponse(USERS, safe=False)
    else:
        return JsonResponse({'sucsses': False, 'error': f'Method {request.method} not allowed'},
                            content_type="application/json", status=405)


def show(request, id):
    if request.method == 'GET':
        if id in range(len(USERS) + 1):
            return JsonResponse(USERS[id - 1], safe=False)
        else:
            return JsonResponse({'sucsses': False, 'error': f'User with id = {id} don\'t exist '},
                                content_type="application/json", status=404)
    else:
        return JsonResponse({'sucsses': False, 'error': f'Method {request.method} not allowed'},
                            content_type="application/json", status=405)


def create(request):
    if request.method == 'POST':
        USERS.append({'id': len(USERS) + 1, 'name': request.POST.get("name"), 'surname': request.POST.get("surname"),
                      'birthday': request.POST.get("birthday"), 'gender': request.POST.get("gender")})
        return JsonResponse(USERS[-1], safe=False)
    else:
        return JsonResponse({'sucsses': False, 'error': f'Method {request.method} not allowed'},
                            content_type="application/json", status=405)
