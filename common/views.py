from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserForm


def signup(request):
    """
    계정생성
    """
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})

# https://stackoverflow.com/questions/60507625/django-wrong-amount-of-arguments-in-custom-handler
# 장고 버전에 따라서, 이렇게 해야지 에러가 안남.
def page_not_found(request, exception):
    """
    404 Page not found
    """
    return render(request, 'common/404.html', {})

def server_error(request, *args, **argv):
    """
    500 Server Error
    """
    print('werwerrw')
    return render(request, 'common/500.html', {})


