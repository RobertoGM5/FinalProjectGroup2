# messaging/forms.py
from django import forms

class MessageForm(forms.Form):
    recipient_email = forms.EmailField(label='Recipient Email')
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
