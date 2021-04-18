from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def userLogin(request):
    form2 = UserForm()
    if request.method == 'POST':
        form1 = UserLoginForm(data=request.POST)
        if form1.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                
                login(request, user)
                if request.POST.get('check') == "check":
                    request.session.set_expiry(0)
                return redirect('home:index')
            else:
                print('i am not logged in')
                message = "Either user does not exists or password not correct. Please try again."
                context = {'form1': form1, 'form2': form2, 'message':message}
                return render(request, 'accounts/login.html', context)
    else:
        form1 = UserLoginForm()
    context = {'form1':form1, 'form2':form2}
    return render(request, 'accounts/login.html', context)

def userLogout(request):
    logout(request)
    request.session.clear_expired()
    return redirect('accounts:login')

def acc_register(request):
    form1 = UserLoginForm()
    if request.method == 'POST':
        form2 = UserForm(data=request.POST)
        if form2.is_valid():
            username = form2.cleaned_data.get('username')
            first_name = form2.cleaned_data.get('first_name')
            last_name = form2.cleaned_data.get('last_name')
            email = form2.cleaned_data.get('email')
            password = form2.cleaned_data.get('password1')
            form2.save()
            user = User.objects.get(username=username)
            login(request, user)
            return redirect('home:index')
    else:
        form2 = UserForm()
    context = {'form1':form1, 'form2':form2}
    return render(request, 'accounts/login.html', context)


################################ USER PROFILE #########################
def address(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            name = form2.cleaned_data.get('name')
            address_1 = form2.cleaned_data.get('address_1')
            address_2 = form2.cleaned_data.get('address_2')
            area = form2.cleaned_data.get('area')
            region = form2.cleaned_data.get('region')
            country = form2.cleaned_data.get('country')
            pin = form2.cleaned_data.get('pin')
            form.save()
            return redirect('checkout:payment')
    else:
        form = AddressForm()
        context = {'form':form}
    return render(request, 'checkout/checkout.html', context)

