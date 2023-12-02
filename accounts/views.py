from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm


User = get_user_model()

# Create your views here.
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if email and password:
            user = authenticate(request, email=email, password=password)

            if user is not None:
                auth_login(request, user)
                return redirect('index')
            else:
                messages.error(request, 'Invalid email or password')
        else:
            messages.error(request, 'Please provide both email and password')
    return render(request, 'pages/login.html')
    
    
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        try:
            if form.is_valid():
                
                    form.save()
                    email = form.cleaned_data['email']
                    password = form.cleaned_data['password1']
                    user = authenticate(email=email, password=password)
                    if user is not None:
                        auth_login(request, user)
                        messages.success(request, 'Registration successful! You are now logged in.')
                        return redirect('index')
        except ValueError as e:
                form.add_error(e)
    else:
        form = CustomUserCreationForm()

    return render(request, 'pages/register.html', {'form': form})