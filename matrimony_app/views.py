from django.shortcuts import render
from django.http import HttpResponse
from .forms import SignupForm,RegistrationForm

# Create your views here.

def homepage(request):
    return render(request,'matrimony/homepage.html')


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            return HttpResponse('/')
    else:
        form = SignupForm()
    return render(request,'matrimony/signup.html',{'form':form})



def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()
            return HttpResponse('/')
    else:
        form = RegistrationForm()
    return render(request,'matrimony/registration.html',{'form':form})