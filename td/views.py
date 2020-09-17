from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your views here.
def signupuser(request):
    if request.method == 'GET':
        return render(request ,'signupuser.html',{'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(request.POST['username'])
            user.save()
        else:
            return render(request ,'signupuser.html',{'form':UserCreationForm(), 'error':'Password did not matgch'})