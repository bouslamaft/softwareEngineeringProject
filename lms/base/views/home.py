from django.http import HttpResponseRedirect
from django.shortcuts import render


def home_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')

    return render(request, 'index.html')  # Fathi view
