from django.contrib import admin
from .models import User

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display =('first_name','last_name','email','phone_number','registration_date',)
    search_fields = ('first_name','email')
    list_filter = ('first_name','email',)
