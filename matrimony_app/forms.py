from django import forms
from .models import User, Registration



class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','email','phone_number','password')
        widgets = {
            'password':forms.PasswordInput(),
        }


class BasicInfoForm(forms.ModelForm):
    MARTIAL = [
        ('Never Married', 'Never Married'),
        ('Widow', 'Widow'),
    ]
    martial = forms.ChoiceField(choices=MARTIAL)

    class Meta:
        model = Registration
        fields = ('profile_for','gender','religion','mother_tongue','martial')


class PhysicalCharcForm(forms.ModelForm):
    height_ft_in_cms = forms.IntegerField()
    weight_in_kgs = forms.IntegerField()
    BODY_TYPE_CHOICES = [
    ('Slim','Slim'),
    ('Average','Average'),
    ('Athletic','Athletic'),
    ('Heavy','Heavy'),
    ]
    body_type = forms.ChoiceField(choices=BODY_TYPE_CHOICES)
    COMPLEXION_CHOICES = [
    ('Very Fair','Very Fair'),
    ('Fair','Fair'),
    ('Wheatish','Wheatish'),
    ('Wheatish Brown','Wheatish Brown'),
    ]
    complexion = forms.ChoiceField(choices=COMPLEXION_CHOICES)
    PHYSICAL_STATUS = [
    ('Normal','Normal'),
    ('Physically Challenged','Physically Challenged'),
    ]
    physical_status = forms.ChoiceField(choices=PHYSICAL_STATUS)

    class Meta:
        model = Registration
        fields = ('height_ft_in_cms','weight_in_kgs','body_type','complexion','physical_status',)


class EducationForm(forms.ModelForm):
    highest_education = forms.CharField(max_length=50)
    EMPLOYMENT_TYPE_CHOICES = [
        ('Government','Government'),
        ('Private','Private'),
        ('Business','Business'),
        ('Defence','Defence'),
        ('Self Employed','Self Employed'),
    ]
    employment_type = forms.ChoiceField(choices=EMPLOYMENT_TYPE_CHOICES)
    occupation = forms.CharField(max_length=50)
    income = forms.CharField(max_length=20)

    class Meta:
        model = Registration
        fields = ('highest_education','employment_type','occupation','income',)


class AstrologyInfoForm(forms.ModelForm):
    star = forms.CharField(max_length=50)
    zodiac_sign = forms.CharField(max_length=50)

    class Meta:
        model = Registration
        fields = ('star','zodiac_sign')

class HabitForm(forms.ModelForm):
    FOOD_HABITS_CHOICE = [
        ('Vegetarian','Vegetarian'),
        ('Non-Vegetarian','Non-Vegetarian'),
        ('Eggetarian','Eggetarian'),
    ]
    food_habits = forms.ChoiceField(choices=FOOD_HABITS_CHOICE)
    SMOKING_CHOICE = [
        ('No','No'),
        ('Occasionally','Occasionally'),
        ('Yes','Yes'),
    ]
    smoking = forms.ChoiceField(choices=SMOKING_CHOICE)
    DRINKING_CHOICE = [
        ('No','No'),
        ('Occasionally','Occasionally'),
        ('Yes','Yes'),
    ]
    drinking = forms.ChoiceField(choices=DRINKING_CHOICE)

    class Meta:
        model = Registration
        fields = ('food_habits','smoking','drinking',)
    

class FamilyProfileForm(forms.ModelForm):
    FAMILY_STATUS_CHOICE = [
        ('Middle Class','Middle Class'),
        ('Upper Middle Class','Upper Middle Class'),
        ('Rich','Rich'),
        ('Affluent','Affluent'),
    ]
    family_status = forms.ChoiceField(choices=FAMILY_STATUS_CHOICE)
    FAMILY_TYPE_CHOICE = [
        ('Joint Family','Joint Family'),
        ('Nuclear Family','Nuclear Family'),
        ('Others','Others'),
    ]
    family_type = forms.ChoiceField(choices=FAMILY_TYPE_CHOICE)
    FAMILY_VALUES_CHOICE = [
        ('Orthodox','Orthodox'),
        ('Moderate','Moderate'),
        ('Traditional','Traditional'),
        ('Liberal','Liberal'),
    ]
    family_values = forms.ChoiceField(choices=FAMILY_VALUES_CHOICE)
    parent_phone_number = forms.CharField(max_length=10)

    class Meta:
        model = Registration
        fields = ('family_status','family_type','family_values','parent_phone_number',)

