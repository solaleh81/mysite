from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect


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




def logout_view(request):
    return render(request, 'accounts/logout.html')


def signup_view(request):
    return render(request, 'accounts/signup.html')
