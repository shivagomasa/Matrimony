from django.shortcuts import render
from django.http import HttpResponse
from .forms import SignupForm

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