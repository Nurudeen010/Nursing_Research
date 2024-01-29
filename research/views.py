from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from .models import ResearchModel
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

def index(request):
    """Render the index page."""
    return render(request, 'research/index.html')

def RegisterView(request):
    """Handle user registration."""
    form = RegisterForm()

    if request.method == 'POST':
        # Process form submission
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("homepage")
    
    context = {
        "form" : form
    }

    return render(request, 'research/register.html', context=context)

def loginView(request):
    """Handle user login."""
    loginform = LoginForm()

    if request.method == 'POST':
        # Process form submission
        loginform = LoginForm(request, data=request.POST)
        if loginform.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    else:
        loginform = LoginForm()

    return render(request, 'research/login.html', {"loginform" : loginform})

def logoutView(request):
    """Handle user logout."""
    logout(request)
    return redirect('login')

@login_required(login_url="login")
def dashboardView(request):
    """Render the dashboard, showing research data."""
    research = ResearchModel.objects.all()
    return render(request, 'research/dashboard.html', {"research": research})

def aboutView(request):
    """Render the about page."""
    return render(request, 'research/about.html')
