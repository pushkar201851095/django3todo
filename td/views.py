from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import TodoForm
# Create your views here.

def home(request):
    return render(request, 'home.html')
def signupuser(request):
    if request.method == 'GET':
        return render(request ,'signupuser.html',{'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'])
                user.save()
                login(request, user)
                return redirect('currenttodos')

            except IntegrityError:
                return render(request ,'signupuser.html',{'form':UserCreationForm(), 'error':'That username has already been taken please choose different user name!!'})                    
        else:
            return render(request ,'signupuser.html',{'form':UserCreationForm(), 'error':'Password did not match'})

def loginuser(request):
    if request.method == 'GET':
        return render(request ,'loginuser.html',{'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'loginuser.html',{'form':AuthenticationForm(),'error':'Username and Password did not match!!'})
        else:
            login(request, user)
            return redirect('currenttodos')

def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')



def currenttodos(request):
    return render(request, 'currenttodos.html')

def createtodo(request):
    if request.method == 'GET':
        return render(request ,'createtodo.html',{'form':TodoForm()})    
    else:
        pass