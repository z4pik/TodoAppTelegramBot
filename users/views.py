from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from todo_app.models import Task
from .forms import UserEditForm


def register(request):
    """Регистрация"""
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Создан аккаунт {username}!')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def profile(request):
    """Профиль пользователя"""
    tasks = Task.objects.filter(user=request.user.id)
    context = {
        "tasks": tasks,
    }
    return render(request, 'users/profile.html', context)


def edit_user(request):
    user = request.user

    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserEditForm(instance=user)

    return render(request, 'users/edit_user.html', {'form': form})
