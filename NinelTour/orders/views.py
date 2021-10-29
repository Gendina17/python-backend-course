from django.http import JsonResponse, HttpResponseNotAllowed
from users.views import USERS
from packages.views import PACKAGES

ORDERS = [{'id': 1, 'user_id': 1, 'date': '20-12-2021', 'package_id': 1, 'count_users': 3,
           'count_children': 1, 'state': 'booked', 'number_rest_days': 7},
          {'id': 2, 'user_id': 2, 'date': '30-12-2022', 'package_id': 2, 'count_users': 1,
           'count_children': 1, 'state': 'trip', 'number_rest_days': 14},
          {'id': 3, 'user_id': 1, 'date': '10-10-2021', 'package_id': 3, 'count_users': 2,
           'count_children': 2, 'state': 'paid', 'number_rest_days': 5}]


def index(request):
    if request.method == 'GET':
        orders = []
        for order in ORDERS:
            order['package'] = PACKAGES[order['package_id'] - 1]
            order['user'] = USERS[order['user_id'] - 1]
            orders.append(order)
        return JsonResponse(orders, safe=False)
    else:
        raise HttpResponseNotAllowed(f'Method {request.method} not allowed')


def show(request, user_id):
    if request.method == 'GET':
        orders = []
        for order in ORDERS:
            if order['user_id'] == user_id:
                order['package'] = PACKAGES[order['package_id'] - 1]
                order['user'] = USERS[order['user_id'] - 1]
                orders.append(order)
        return JsonResponse(orders, safe=False)
    else:
        raise HttpResponseNotAllowed(f'Method {request.method} not allowed')


def create(request):
    if request.method == 'POST':
        ORDERS.append({'id': len(PACKAGES) + 1, 'user_id': request.POST.get("user_id"),
                       'date': request.POST.get("date"), 'package_id': request.POST.get("package_id"),
                       'count_users': request.POST.get("count_users"),
                       'count_children': request.POST.get("count_children"),
                       'state': request.POST.get("state"), 'number_rest_days': request.POST.get("number_rest_days")})
        return JsonResponse(ORDERS[-1], safe=False)
    else:
        raise HttpResponseNotAllowed(f'Method {request.method} not allowed')
