from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.


def signup(request):
    if request.method == 'POST':
        username = request.POST['first_name']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username already exists')
                return redirect('signup')
            else:
                # create user and profile objects
                user = User.objects.create_user(username=username, password=password,)
                user.save()               

                messages.success(request, 'Account created successfully.')
                return redirect('home')
        else:
            messages.info(request, 'Both passwords are not matching')
            return redirect('signup')

    return render(request, 'signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            if request.POST.get('remember_me'):
                # Persistent session for 14 days
                request.session.set_expiry(1209600)
            else:
                # Browser-length session
                request.session.set_expiry(0)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'signin.html')

@login_required(login_url="signin")
def home_view(request):
    if not request.user.is_authenticated:
        return redirect('signin')  
    return render(request, 'home.html')

def logout_view(request):
    logout(request)
    return redirect('signin') 
