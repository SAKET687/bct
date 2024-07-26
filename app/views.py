from django.shortcuts import render, redirect
from .models import Users
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import login as auth_login

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        try:
            user = Users.objects.get(username=username)
            if check_password(password, user.password):
                auth_login(request, user)
                return redirect("home")  # Redirect to the home view
            else:
                return render(request, "login.html", {"error": "Invalid Password"})
        except Users.DoesNotExist:
            return render(request, "login.html", {"error": "User Does Not Exist"})
    else:
        return render(request, "login.html")

def register(request):
    if request.method == "POST":
        name = request.POST["name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        hashed_password = make_password(password)
        user = Users(
            name=name,
            username=username,
            email=email,
            password=hashed_password,
        )
        print(user)
        user.save()
        return redirect("/login")  # Redirect to the login view
    else:
        return render(request, "register.html")

def home_view(request):
    return render(request, "index.html")
