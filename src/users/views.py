from django.shortcuts import render
from django.contrib.auth import authenticate


def login(request):
    if request.method == 'POST':
        username = request.POST["login_username"]
        password = request.POST["login_password"]
        authenticated_user = authenticate(username=username, password=password)
        if len(authenticated_user) > 0:
            print("Usuario correcto")
        else:
            print("Usuario incorrecto")
    else:
        return render(request, "404.html")

    return render(request, "login_form.html")
