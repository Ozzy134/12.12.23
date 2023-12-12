from django.shortcuts import render
from .forms import UserForm
from django.http import HttpResponse
from .forms import VxodForm, Reg
from .models import Person, Posts

def data(request):
    tom = Person.objects.get_or_create(name='Tom', age=14, date='2015-02-03 10:53:55', agree=False)

    mike = Person(name='Mike_Afton', age=25, date='2015-02-03 10:53:55')
    mike.save()
    data = Person.objects.all()
    return render(request, 'app/data.html', context={'data': data})

def posts(request):
    post = Posts.objects.all()
    return render(request, 'app/post.html', context={'posts': post})

def index(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            email = form.cleaned_data['email']
            return HttpResponse(f'Name: {name}, Age {age}, Email: {email}')
        else:
            return HttpResponse('Date no base!')
    else:
        form = UserForm()
        return render(request, 'app/index.html', context={'form': form})

def vxod(request):
    if request.method == "POST":
        form = VxodForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            if email == 'User1' and password == 123456:
                return HttpResponse(f'{name}, Поздравляю со входом!')
            else:
                return HttpResponse('Error!')
        else:
            return HttpResponse('Date no base!')
    else:
        form = VxodForm()
        return render(request, 'app/vxod.html', context={'form': form})

def reg(request):
    if request.method == "POST":
        form = Reg(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            return HttpResponse(f'{name}, Поздравляю с регистрацией!')
        else:
            return HttpResponse('Date no base!')
    else:
        form = Reg()
        return render(request, 'app/reg.html', context={'form': form})