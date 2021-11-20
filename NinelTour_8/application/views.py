from django.shortcuts import render, redirect
from rest_framework import viewsets


def login_required(function):
    def check_authenticate(*args, **kwargs):
        if len(args) > 1:
            request = args[1]
        else:
            request = args[0]

        if request.user.is_authenticated:
            return function(*args, **kwargs)
        else:
            return redirect('login')

    return check_authenticate


@login_required
def index(request):
    return render(request, 'index.html', {
        'name': request.user.first_name,
        'surname': request.user.last_name})


def login(request):
    return render(request, 'login.html')


class UniversalViewSet(viewsets.ModelViewSet):
    @login_required
    def list(self, request, *args, **kwargs):
        return super(UniversalViewSet, self).list(request, *args, **kwargs)

    @login_required
    def create(self, request, *args, **kwargs):
        return super(UniversalViewSet, self).create(request, *args, **kwargs)

    @login_required
    def retrieve(self, request, *args, **kwargs):
        return super(UniversalViewSet, self).retrieve(request, *args, **kwargs)

    @login_required
    def update(self, request, *args, **kwargs):
        return super(UniversalViewSet, self).update(request, *args, **kwargs)

    @login_required
    def partial_update(self, request, *args, **kwargs):
        return super(UniversalViewSet, self).partial_update(request, *args, **kwargs)

    @login_required
    def destroy(self, request, *args, **kwargs):
        return super(UniversalViewSet, self).destroy(request, *args, **kwargs)
