from django.urls import path
from .views import support_request

app_name = 'support'

urlpatterns = [
    path('', support_request, name='support_request'),
]
