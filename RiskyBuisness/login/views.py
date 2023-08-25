from django.shortcuts import render
from .forms import LoginForm
from django.http import HttpResponseRedirect
from .models import Member
from .forms import MemberForm

def login_show(request):

    if request.method == "POST":
        
        form = LoginForm(request.POST)
        if form.is_valid():
            form.cleaned_data
            
            user = Member.objects.filter(username=form.cleaned_data['username']).values()

            if user and (user[0]['password'] == form.cleaned_data['password']):
                request.session["username"] = form.cleaned_data['username']
                request.session["password"] = form.cleaned_data['password']
                return HttpResponseRedirect('/')
            
            else:
                return render(request, "login.html", {"msg": 'Incorrect username or password.', "form": form})
      
    else:
        form = LoginForm()

    return render(request, "login.html", {"form": form})

def signup_show(request):

    if request.method == "POST":
        
        form = MemberForm(request.POST)
        if form.is_valid():
            form.cleaned_data
            
            user = Member.objects.filter(username=form.cleaned_data['username']).values()

            print(user)

            if not user:
                request.session["username"] = form.cleaned_data['username']
                request.session["password"] = form.cleaned_data['password']
                form.save()
                return HttpResponseRedirect('/')
            
            else:
                return render(request, "signup.html", {"msg": 'Username is already in use.', "form": form})

    else:
        form = LoginForm()

    return render(request, "signup.html", {"form": form})