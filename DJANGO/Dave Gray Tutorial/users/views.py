from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse


# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # login
            login(request, user)
            return HttpResponseRedirect(reverse("users:dashboard"))
        # else:
        #     return render(request, "users/register.html", {"form": form})
    else:
        form = UserCreationForm()
    return render(request, "users/register.html", {"form": form})


# In Django, a view function must always return an HttpResponse object or an HttpResponseRedirect
# if form is invalid still it renders the register.html with error message as HttpRespnse Object.
def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        # * here instead of request.POST, we used data= request.POST  because data is the keyword argument required to be passed
        if form.is_valid():
            login(request, form.get_user())
            return redirect("users:dashboard")
    else:
        form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form})


@login_required
def dashboard(request):
    return render(request, "users/dashboard.html")


def logout_view(request):
    logout(request)
    return redirect("users:login_user")
