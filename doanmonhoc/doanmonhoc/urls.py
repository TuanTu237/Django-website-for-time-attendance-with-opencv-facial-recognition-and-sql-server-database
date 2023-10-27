
from django.contrib import admin
from django.urls import path
from core.views import index,login, signup
urlpatterns = [
    path('login/',login,name='login'),
    path('signup',signup,name='signup'),
    path('',index, name='index'),
    path("admin/", admin.site.urls),
]
