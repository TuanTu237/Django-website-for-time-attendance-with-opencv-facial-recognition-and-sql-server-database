
from django.contrib import admin
from django.urls import path
from core.views import index,login, signup,slidebar,slideNV,loginNV,loginQL
urlpatterns = [
    path('login/',login,name='login'),
    path('loginNV/',loginNV,name='loginNV'),
    path('loginQL/',loginQL,name='loginQL'),
    path('signup',signup,name='signup'),
    path('slidebar',slidebar,name='slidebar'),
    path('slideNV',slideNV,name='slideNV'),
    path('',index, name='index'),
    path("admin/", admin.site.urls),
    
]
