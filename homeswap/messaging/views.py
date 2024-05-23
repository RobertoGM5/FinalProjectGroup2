from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from .forms import MessageForm
from django.conf import settings

@login_required
def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            recipient_email = form.cleaned_data['recipient_email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender_email = request.user.email

            # Send email to recipient
            recipient_message = f"You have received a message from {sender_email} through our Homeswap website:\n\n{message}"
            send_mail(subject, recipient_message, settings.DEFAULT_FROM_EMAIL, [recipient_email])

            # Send confirmation email to sender
            confirmation_message = f"You have sent the following message to {recipient_email}:\n\n{message}"
            send_mail('Message Sent Confirmation', confirmation_message, settings.DEFAULT_FROM_EMAIL, [sender_email])

            return redirect('messaging:message_sent')
    else:
        form = MessageForm()
    return render(request, 'messaging/send_message.html', {'form': form})

def message_sent(request):
    return render(request, 'messaging/message_sent.html')
