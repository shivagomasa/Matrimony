from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import login_required
from .forms import SignupForm,BasicInfoForm,PhysicalCharcForm,EducationForm,AstrologyInfoForm,HabitForm,FamilyProfileForm
from django.db import transaction
from django.contrib.auth import get_user_model

# Create your views here.

User = get_user_model()


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
        return render(request, 'registration/signup.html', {'form':form})


@login_required
@transaction.atomic
def registration(request):
    if request.method == 'POST':
        register_form = BasicInfoForm(request.POST)
        physical_form = PhysicalCharcForm(request.POST)
        edu_form = EducationForm(request.POST)
        astr_form = AstrologyInfoForm(request.POST)
        habit_form = HabitForm(request.POST)
        family_form = FamilyProfileForm(request.POST)

        if register_form.is_valid() and physical_form.is_valid() and astr_form.is_valid() and habit_form.is_valid() and family_form.is_valid():
            r_form = register_form.save(commit=False)
            r_form.user = request.user
            r_form.save()
            physical_form.save()
            astr_form.save()
            habit_form.save()
            family_form.save()
            return redirect('/')
        if edu_form.is_valid():
            edu_form.save()
    
    else:
        register_form = BasicInfoForm()
        physical_form = PhysicalCharcForm()
        edu_form = EducationForm()
        astr_form = AstrologyInfoForm()
        habit_form = HabitForm()
        family_form = FamilyProfileForm()
        frontend = {
        'register_form':register_form,
        'physical_form':physical_form,
        'edu_form':edu_form,
        'astr_form':astr_form,
        'habit_form':habit_form,
        'family_form':family_form,

        }
    
    return render(request, 'registration/registration.html',frontend)
