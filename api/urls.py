from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [

    path('ticket/', views.ticketlist.as_view()),
    path('bookticket/', views.bookticket.as_view()),

]
