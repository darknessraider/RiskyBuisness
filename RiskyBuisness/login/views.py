from django.shortcuts import render
from .forms import LoginForm
from django.http import HttpResponseRedirect

def login_show(request):
    if request.method == "POST":
        
        form = LoginForm(request.POST)
        if form.is_valid():
            form.cleaned_data
            request.session["username"] = form.cleaned_data['username']
            request.session["password"] = form.cleaned_data['password']
            return HttpResponseRedirect('/')
    else:
        form = LoginForm()

    return render(request, "login.html", {"form": form})
