from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import Sign_Up, Sign_In, Add
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
import random
from .models import Post
# Create your views here.


def index(request):
    return HttpResponseRedirect('sign_up_page')


def sign_up_page(request):
    form = Sign_Up()
    a = random.randint(0, 9)
    b = random.randint(0, 9)
    c = a+b
    global d
    d = str(c)
    #print("I am a Sign_up_page","&&&&&&&",a,"##########",b,"@@@@@@",c)
    return render(request, 'sign_up.html', {'fm': form, 'a': a, "p": "+", "b": b})


def sign_up(request):
    if request.method == "POST":
        form = Sign_Up(request.POST)
        #print("i am check validity", d,form.is_valid())
        if form.is_valid():
            captcha = request.POST.get("cap")
            #print("i am inner the form_is valid()", d, captcha,form.is_valid())
            if d == (captcha):
                messages.success(
                    request, "Congratulations !!!!!Your Account is Created.")
                form.save()
                return redirect('/sign_in')
            else:
                messages.warning(request,'Enter Captcha is Invalid')
                return redirect('/sign_up_page')
        #return redirect('sign_up_page')
        a = random.randint(0, 9)
        b = random.randint(0, 9)
        c = a+b
        #print("&&&&&&&",a,"##########",b,"@@@@@@",c)
        return render(request, 'sign_up.html', {'fm': form, 'a': a, "p": "+", "b": b})

        
def sign_in(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = Sign_In(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in successfully')
                    return HttpResponseRedirect('/dashboard')
        else:
            form = Sign_In()
        return render(request, 'sign_in.html', {'form': form})
    else:
        return HttpResponseRedirect('/dashboard')


def sign_out(request):
    logout(request)
    return HttpResponseRedirect('sign_in')


def dashboard(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        user = request.user
        posts = Post.objects.filter(user=user)
        return render(request, 'dashboard.html', {'posts': posts, 'full_name': user})
    else:
        return HttpResponseRedirect('sign_in')


def add(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            a = Add(request.POST, request.FILES)
            if a.is_valid():
                tit = a.cleaned_data['title']
                des = a.cleaned_data['desc']
                stat = a.cleaned_data['status']
                img = a.cleaned_data['image']
                user = request.user
                fm = Post(title=tit, desc=des, status=stat,
                          user=user, image=img)
                fm.save()
                messages.success(request, "Post Added Successfully")
                return HttpResponseRedirect('dashboard')
        else:
            a = Add()
            return render(request, 'add.html', {'a': a})
    else:
        return HttpResponseRedirect('sign_in')


def search(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            n = request.POST.get('search')
            a = User.objects.filter(username=n).exists()
            posts = Post.objects.filter(status="public").filter(user=n)
            if a is True:
                return render(request, 'dashboard.html', {'posts': posts, "user": n})
            else:
                return render(request, 'dashboard.html', {'posts': posts, "user": n})
    else:
        return HttpResponseRedirect('sign_in')
