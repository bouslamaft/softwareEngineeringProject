from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.http import HttpResponseRedirect
from django.contrib.auth.models import Group
from django.contrib import auth
from django.contrib.auth.decorators import login_required,user_passes_test
from datetime import datetime,timedelta,date
from django.core.mail import send_mail


def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    # return render(request,'index.html')
    return render(request ,'index.html' ) # Fathi view

def student(request):
    return render(request , 'library/student.html')
    #add your code here 
def studentlogin(request):
    return render(request, 'login/studentlogin.html')

def studentsignup(request):
    return render(request , 'login/studentsignup.html')

def librarian(request):
    return render (request, 'library/librarian.html')

def librarianlogin(request):
    return render(request , 'login/librarianlogin.html')

def afterlogin_view(request):
    return 

def aboutus_view(request):
    return render(request,'base/aboutus.html')

def contactus_view(request):
    sub = forms.ContactusForm()
    if request.method == 'POST':
        sub = forms.ContactusForm(request.POST)
        if sub.is_valid():
            email = sub.cleaned_data['Email']
            name=sub.cleaned_data['Name']
            message = sub.cleaned_data['Message']
            send_mail(str(name)+' || '+str(email),message, EMAIL_HOST_USER, ['a@gmail.com'], fail_silently = False)
            return render(request, 'base/contactussuccess.html')
    return render(request, 'base/contactus.html', {'form':sub})    