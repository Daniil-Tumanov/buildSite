from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

from buildApp.forms import AuthUserForm

from buildApp.models import Service, Category


def index(request):
    return render(request, 'buildApp/index.html')


def about(request):
    return render(request, 'buildApp/about.html')


def service(request):
    service = Service.objects.all()
    category = Category.objects.all()
    return render(request, 'buildApp/service.html', {"service": service, "category": category})


def contacts(request):
    return render(request, 'buildApp/contacts.html')


class Logout(LogoutView):
    next_page = reverse_lazy('index')


class BuildLoginView(LoginView):
    template_name = 'buildApp/login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('index')


def registerPage(request):
    if request.method == 'POST':
        user = User()
        user.first_name = request.POST.get("FirstName")
        user.last_name = request.POST.get("LastName")
        user.email = request.POST.get("Email")
        user.username = request.POST.get("Login")
        user.set_password(request.POST.get("Password"))
        user.save()
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        login(request, user)
        next_page = reverse_lazy('index')
        context = {
            'form': f"<h1 class='center-block'>Регистрация успешно завершена. <br>Здравствуйте, <h1 color='red'{user.first_name} {user.last_name}!</h1> Добро пожаловать</h1>:"}
        return render(request, 'buildApp/index.html', context)
