from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import SupportForm


def support_request(request):
    thank_you_message = False
    if request.method == 'POST':
        support_form = SupportForm(request.POST)
        if support_form.is_valid():
            support_form.save()
            send_support_email(support_form.cleaned_data['email'])
            thank_you_message = True
    else:
        support_form = SupportForm()
        print(support_form)
    return render(request, 'home.html', {'support_form': support_form, 'thank_you_message': thank_you_message})


def send_support_email(email):
    subject = 'Thank you for your support request'
    message = 'We have received your support request and will respond as soon as possible.'
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email])
