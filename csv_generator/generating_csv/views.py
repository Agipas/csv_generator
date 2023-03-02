from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView

from .decorators import user_not_authenticated
from .forms import LoginUserForm
from .models import *


@login_required
def index(request):
    return render(request, 'base.html')


@login_required
def logout_user(request):
    logout(request)
    return redirect('login')


@method_decorator(user_not_authenticated, name='dispatch')
class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'

    def get_success_url(self):
        return reverse_lazy('index')


def error_404_view(request, exception):
    return render(request, '404.html')


def new_scheme(request):
    if request.method == 'GET':
        schemes = DataScheme.objects.all()
        print(schemes)
        return render(request, 'data_scheme/create.html', {'schemes': schemes})


class DataSchemePage(ListView):
    model = DataScheme
    template_name = 'data_scheme.html'
    context_object_name = 'schemes'
