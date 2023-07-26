from django.urls import path
from emailapp.views import send_email, email_success

urlpatterns = [
    path('', send_email, name='send_email'),
    path('email-success/', email_success, name='email_success'),
    
]
