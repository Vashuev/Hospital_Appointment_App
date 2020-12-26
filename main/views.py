from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from .decorators import already_login
# Create your views here.
@login_required(login_url='login')
def homePage(request):
    context = {}
    return render(request, 'home.html', context)

@already_login
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, "Account Created Successfully.. for "+ username)
            return redirect('login')
    
    context = {'form': form}
    return redirect(request, 'register.html', context=context)

@already_login
def loginPage(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Username or password is Incorrect!")

    context = {}
    return render(request, 'login.html', context)

@login_required(login_url='login')
def logoutPage(request):
    logout(request)
    return redirect('login')