from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout


# Create your views here.

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("food:index")
    else:
        form = UserCreationForm(request.POST or None)
        return render(request, "user/register.html", {"form": form})


def log_out(request):
    logout(request)
    return render(request, "user/logout.html")
