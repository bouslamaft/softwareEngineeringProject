from django.conf.urls import include
from django.urls import path
from django.contrib.auth.views import LogoutView

from lms.base.views.student import student_view
from lms.base.views.librarian import librarian_view
from lms.base.views.home import home_view
from lms.base.views.about_us import about_us_view
from lms.base.views.list_books import list_books_view
from lms.base.views.authentication import login_view, registration_view


urlpatterns = [
    path('', home_view),

    path('accounts/', include('django.contrib.auth.urls')),
    path('listBooks/', list_books_view),

    path('student/', student_view, name='student'),

    path('librarian/', librarian_view, name='librarian'),


    path('login/', login_view, name='login'),
    path('registration/', registration_view, name='registration'),
    path('logout', LogoutView.as_view(template_name='library/index.html')),

    path('aboutus', about_us_view),
    # path('contactus', views.contactus_view),
]

