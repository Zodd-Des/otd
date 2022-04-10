from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Contact

# Create your views here.

def index(request):
    return render(request, 'index.html')

# function to send the form to backend

def contact(request): 
    if request.method == "POST":
        contact = Contact(name = request.POST.get('name'), email = request.POST.get('email'),
                          phone = request.POST.get('phone'), message = request.POST.get('message'))
        contact.save()

        messages.success(request, 'Message sent successfully!')
        return HttpResponseRedirect('/')                  