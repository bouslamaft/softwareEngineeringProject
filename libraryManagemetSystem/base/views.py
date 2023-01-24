from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib import auth, messages
from django.contrib.auth.models import Group, User
from django.contrib.auth.decorators import login_required,user_passes_test
from datetime import datetime,timedelta,date
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.mail import send_mail

class Book:
  def __init__(self, ISBN, Title, Author, Category, Referrence, Status, Action):
    self.isbn = ISBN
    self.title = Title
    self.author = Author
    self.aategory = Category
    self.is_referrence_only = Referrence
    self.status = Status
    self.Action = Action

def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    # return render(request,'index.html')
    return render(request ,'index.html') # Fathi view

def listBooks(request):
    books = []
    
    for i in range (0,21):
        b1 = Book(i,i,i,i,i,i,i)
        books.append(b1)

    page = request.GET.get('page')
    paginator = Paginator(books, 5) # Show 5 books per page.

    try:
        books_obj = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        books_obj = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        books_obj = paginator.page(page)

    context = {'books_obj': books_obj, 'paginator': paginator}
    return render(request, 'listBooks.html', context)

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