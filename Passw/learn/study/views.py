from django.shortcuts import render
from .forms import UserForm, UserProfileInfo


def index(request):
    return render(request, 'index.html')


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfo
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print("user_form.errors,profile_form.errors")
    else:
        user_form = UserForm()
        profile_form = UserProfileInfo

    return render(request, 'registration.html')


def login(request):
    return render(request, 'login.html', {'user_form': user_form,
                                          'registered': registered,
                                          'profile_form': profile_form})
