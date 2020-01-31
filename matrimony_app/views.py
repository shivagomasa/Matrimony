from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import login_required
from .forms import SignupForm,RegistrationForm
from . models import User

# Create your views here.

def homepage(request):
    return render(request,'matrimony/homepage.html')


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(**form.cleaned_data)
            login(request,user)
            return redirect('homepage')
    else:
        form = SignupForm()
        return render(request,'matrimony/signup.html',{'form':form})


@login_required
def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()
            return redirect('/')
    else:
        form = RegistrationForm()
        return render(request,'matrimony/registration.html',{'form':form})