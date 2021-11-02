from django.http import JsonResponse

PACKAGES = [{'id': 1, 'hotel_name': 'Лазурный берег', 'tour_operator': 'Pegast', 'airline': 'S7',
             'departure_city': 'Москва', 'arrival_city': 'Анталия', 'departure_country': 'Турция'},
            {'id': 2, 'hotel_name': 'Туса Джуса', 'tour_operator': 'Coral', 'airline': 'Aeroflot',
             'departure_city': 'Казань', 'arrival_city': 'Каир', 'departure_country': 'Египет'},
            {'id': 3, 'hotel_name': 'Ласковое море', 'tour_operator': 'TezTour', 'airline': 'UralAirlines',
             'departure_city': 'Санкт-Петербург', 'arrival_city': 'Кемер', 'departure_country': 'Турция'}]


def index(request):
    if request.method == 'GET':
        return JsonResponse(PACKAGES, safe=False)
    else:
        return JsonResponse({'sucsses': False, 'error': f'Method {request.method} not allowed'},
                            content_type="application/json", status=405)


def show(request, departure_country):
    if request.method == 'GET':
        packages = []
        for package in PACKAGES:
            if package['departure_country'] == departure_country:
                packages.append(package)
        return JsonResponse(packages, safe=False)
    else:
        return JsonResponse({'sucsses': False, 'error': f'Method {request.method} not allowed'},
                            content_type="application/json", status=405)


def create(request):
    if request.method == 'POST':
        PACKAGES.append({'id': len(PACKAGES) + 1, 'hotel_name': request.POST.get("hotel_name"),
                         'tour_operator': request.POST.get("tour_operator"), 'airline': request.POST.get("airline"),
                         'departure_city': request.POST.get("departure_city"), 'arrival_city': request.POST.get("arrival_city"),
                         'departure_country': request.POST.get("departure_country")})
        return JsonResponse(PACKAGES[-1], safe=False)
    else:
        return JsonResponse({'sucsses': False, 'error': f'Method {request.method} not allowed'},
                            content_type="application/json", status=405)
