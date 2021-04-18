from django import forms
from .models import *

class ContactForm(forms.ModelForm):

    class Meta():
        model = Contact
        exclude = ('id', 'sent_on', 'read')
        widgets={
            'name' : forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Name'}),
            'email' : forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Email', 'validator':'Emailformat is not correct'}),
            'subject' : forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Subject'}),
            'message' : forms.Textarea(attrs={'class': 'form-control', 'rows':8, 'id':'message', 'placeholder':'Your Message Here'}),
        }
    