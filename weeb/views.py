from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from .forms import *
from .models import *
from .decorators import unauthenticated_user

from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models import Q

#@login_required(login_url='login')


now = timezone.now()

@unauthenticated_user
def loginPage(request):
    return render(request, 'login.html')

@unauthenticated_user
def signUpPage(request):
    form = CreateUserForm()
    
    if request.method == 'POST':
        try:
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('main')
        except:
            print(Exception)
            print("Failed")

    context = {
        'form': form,
    }    
    return render(request, 'public/signup.html', context)

def logoutPage(request):
	logout(request)
	return redirect('main')    

def viewUserMain(request, user):
    user = User.objects.get(username=user)
    userPosts = Post.objects.filter(user=user)
    userPostsT = Post.objects.filter(user=user)

    context = {
        "user": user,
        "posts": userPosts,
        "postsT": userPostsT
    }
    return render(request, 'public/user.html', context)

def ViewMainPage(request):
    return render(request, 'public/index.html')

def ViewType(request, user, type):
    user = User.objects.get(username=user)
    allofthem = Post.objects.filter(Q(user=user) & Q(type=str(type.capitalize())))
    
    context = {
        'type': type,
        'user' : user,
        'posts': allofthem
    }
    return render(request, 'public/section.html', context)

def ViewPost(request, postID):

    post = Post.objects.get(id=postID)

    context = {
        'post': post
    }
    return render(request, 'public/post.html', context)

def ViewAll(request):
    posts = Post.objects.all()
    count = posts.count()

    context = {
        'count':count,
        'posts':posts
    }
    return render(request, 'public/all.html', context)
