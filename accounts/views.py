from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('blog:blog')
        form = AuthenticationForm()
        return render(request, 'accounts/login.html', context={'form': form})
    else:
        return redirect('blog:blog')

@login_required
def logout_view(request):
    logout(request)
    return redirect('blog:blog')


def signup_view(request):
    return render(request, 'accounts/signup.html')
