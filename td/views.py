from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import TodoForm
from .models import Todo
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
    todos = Todo.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, 'currenttodos.html',{'todos':todos})

def createtodo(request):
    if request.method == 'GET':
        return render(request ,'createtodo.html',{'form':TodoForm()})    
    else:
        pass

def viewtodo(request, todo_pk):
    todo = get_object_or_404(Todo, pk= todo_pk,user=request.user)
    if request.method == 'GET':
        form = TodoForm(instance=todo)
        return render(request, 'viewtodo.html',{'todo':todo, 'form':form})
    else:
        try:
            form = TodoForm(request.POST,instance=todo)
            form.save()
            return redirect('currenttodos')
        except ValueError:
            return render(request, 'viewtodo.html',{'todo':todo,'form':form,'error':'Badinfo'})

    
