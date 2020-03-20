from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UseerOurRegistration, ProfileImage, UserUpdateForm, EmaiDeliveryAgree, GenderSelection

def register(request):
    if request.method == "POST":
            form = UseerOurRegistration(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'Аккаунт {username} был успешно создан, введите имя пользователя и парольдля авторизации ')
                return redirect('user')
    else:
        form = UseerOurRegistration()

    return render(request, 'users/registration.html', {'form':form, 'title': 'Регистрация пользователя'})

@login_required
def profile(request):
    if request.method == "POST":
        img_profile = ProfileImage(request.POST, request.FILES, instance = request.user.profile)
        update_user = UserUpdateForm(request.POST, instance = request.user)
        check_profile = EmaiDeliveryAgree(request.POST,  instance = request.user.profile)

        if update_user.is_valid() and img_profile.is_valid() and check_profile.is_valid():
            img_profile.save()
            update_user.save()
            check_profile.save()
            messages.success(request, f'Аккаунт был успешно обновлен ')

            return redirect('profile')

    else:
        img_profile = ProfileImage(instance = request.user.profile)
        update_user = UserUpdateForm(instance = request.user)
        check_profile = EmaiDeliveryAgree(instance = request.user.profile)
        gender_profile = GenderSelection()

    data = {
    'img_profile': img_profile,
    'update_user': update_user,
    'check_profile': check_profile,
    'gender_profile':gender_profile,

    }
    return render(request, 'users/profile.html',data)
