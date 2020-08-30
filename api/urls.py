from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [

    path('ticket/', views.ticketlist.as_view()),
    path('bookticket/', views.bookTicket.as_view()),
    path('updatetime/<str:pk>/', views.updateTicketTime.as_view()),
    path('viewticket/<str:pk>/', views.viewTicket.as_view()),
    path('deleteticket/<str:pk>/', views.deleteTicket.as_view()),
    

]
