from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request ,'library/index.html' )
    #add your code here 

def student(request):
    return render(request , 'library/student.html')
    #add your code here 
def studentlogin(request):
    return render(request, 'library/studentlogin.html')

def studentsignup(request):
    return render(request , 'library/studentsignup.html')

def librarian(request):
    return render (request, 'library/librarian.html')

def librarianlogin(request):
    return render(request , 'library/librarianlogin.html')

