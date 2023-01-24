from django.http import HttpResponseRedirect
from django.shortcuts import render


def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    # return render(request,'index.html')
    return render(request, 'index.html')  # Fathi view
