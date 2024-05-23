from django.urls import path
from . import views

app_name = 'messaging'

urlpatterns = [
    path('send/', views.send_message, name='send_message'),
    path('sent/', views.message_sent, name='message_sent'),
]
