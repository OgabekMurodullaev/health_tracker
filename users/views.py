from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .models import Profile
from users.forms import RegisterForm, LoginForm


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Xush kelibsiz!")
            return redirect('home')

    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Username yoki parol noto'g'ri")
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def profile_view(request):
    profile = get_object_or_404(Profile, user=request.user)
    return render(request, 'users/profile_view.html', {'profile': profile})


@login_required
def profile_edit(request):
    profile = get_object_or_404(Profile, user=request.user)

    if request.method == 'POST':
        bio = request.POST.get('bio')
        birth_date = request.POST.get('birth_date')
        avatar = request.FILES.get('avatar')

        profile.bio = bio
        if birth_date:
            profile.birth_date = birth_date
        if avatar:
            profile.avatar = avatar
        profile.save()

        messages.success(request, "Profilingiz muvaffaqiyatli yangilandi!")
        return redirect('profile_view')

    return render(request, 'users/profile_edit.html', {'profile': profile})