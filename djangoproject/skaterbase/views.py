from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from skaterbase.forms import SignUpForm


# Create your views here.

def Login(request):
    return render(request, 'login.html')

def Home(request):
    return render(request, 'home.html')

def AboutSkater(request):
    return render(request, 'AboutSkater.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('/skaterbase/login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

