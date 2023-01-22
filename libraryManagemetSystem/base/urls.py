"""librarymanagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from . import views


urlpatterns = [
    path('accounts/',include('django.contrib.auth.urls') ),
    path('', views.home_view),
    path('listBooks/', views.listBooks),

    path('student/', views.student , name='student') ,
    path('student/studentlogin/' , views.studentlogin, name = 'studentlogin'),
    path('student/studentsignup/' , views.studentsignup , name='studentsignup') , 
    
    path('librarian/', views.librarian , name = 'librarian'),
    path('librarian/librarianlogin/' , views.librarianlogin , name='librarianlogin' ), 

    

    path('logout', LogoutView.as_view(template_name='library/index.html')),
    path('afterlogin', views.afterlogin_view),

    path('aboutus', views.aboutus_view),
    path('contactus', views.contactus_view),

]
