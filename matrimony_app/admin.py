from django.contrib import admin
from .models import User,Registration
from .forms import BasicInfoForm
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display =('first_name','last_name','email','phone_number','registration_date',)
    search_fields = ('first_name','email')
    list_filter = ('first_name','email',)



class RegistrationAdmin(admin.ModelAdmin):
    form = BasicInfoForm
    list_display = ('user','profile_for','gender','religion','mother_tongue',)
    search_fields = ('gender','religion','mother_tongue',)
    list_filter = ('gender','religion',)


admin.site.register(User)
admin.site.register(Registration, RegistrationAdmin)
