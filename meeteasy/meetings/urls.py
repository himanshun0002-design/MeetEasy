from django.contrib import admin
from django.urls import path
from meetings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'), 
]
