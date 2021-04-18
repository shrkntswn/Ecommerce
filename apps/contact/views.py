from django.shortcuts import render
from .forms import *

def contact(request):
    message =""
    if request.method == 'POST':
        form = ContactForm(data = request.POST )
        if form.is_valid():
            form.save()
            
    form = ContactForm()
    context = {'form':form}
    return render(request, 'contact/contact.html', context)
