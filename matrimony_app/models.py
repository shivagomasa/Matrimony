from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.conf import settings

from .managers import UserManager
# Create your models here.

class User(AbstractBaseUser,PermissionsMixin):
    first_name = models.CharField(_('first name'),max_length=100,blank=True)
    last_name = models.CharField(_('last name'),max_length=100,blank=True)
    email = models.EmailField(_('email'),unique=True,blank=True)
    phone_number = models.CharField(_('phone number'),max_length=10,blank=True)
    password = models.CharField(_('password'),max_length=120,blank=True)
    is_staff = models.BooleanField(_('staff'),default=True)
    is_active = models.BooleanField(_('active'),default=True)
    registration_date = models.DateTimeField(_('registered date'),default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        return '%s %s' % (self.first_name,self.last_name)


class Registration(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    PROFILE_CHOICES = [
        ('Myself','Myself'),
        ('Son','Son'),
        ('Daughter','Daughter'),
        ('Brother','Brother'),
        ('Sister','Sister'),
        ('Friend','Friend'),
        ('Relative','Relative'),
    ]
    profile_for = models.CharField(choices=PROFILE_CHOICES,max_length=10)
    GENDER_CHOICES = [
        ('Male','Male'),
        ('Female','Female'),
    ]
    gender = models.CharField(choices=GENDER_CHOICES,max_length=10)
    RELIGION_CHOICES = [
        ('Hindu','Hindu'),
        ('Muslim','Muslim'),
        ('Christian','Christian'),
        ('Sikh','Sikh'),
        ('Buddist','Buddist'),
    ]
    religion = models.CharField(choices=RELIGION_CHOICES,max_length=10)
    MOTHER_TONGUE_CHOICES = [
        ('Hindi','Hindi'),
        ('English','English'),
        ('Marathi','Marathi'),
        ('Telugu','Telugu'),
        ('Tamil','Tamil'),
    ]
    mother_tongue = models.CharField(choices=MOTHER_TONGUE_CHOICES,max_length=10)

    def __str__(self):
        return self.user

