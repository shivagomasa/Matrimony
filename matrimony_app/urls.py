from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [

    path('',views.homepage,name='homepage'),
    path('signup/',views.signup,name='signup'),
    path('registration',views.registration,name='registration'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),

]