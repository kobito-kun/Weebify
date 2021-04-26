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

@login_required(login_url='login')
def dashboardPage(request):

    totalPosts = Post.objects.filter(user=request.user)
    tenPosts = Post.objects.filter(user=request.user)[0:10]

    context = {
        'postsT':totalPosts,
        'posts':tenPosts
    }
    return render(request, 'dashboard.html', context)

@login_required(login_url='login')
def addPostDashboardPage(request):

    form = PostForm()

    if request.method == 'POST':
        user = User.objects.get(username=request.user)
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            post.user = user
            post.save()
            return redirect("dashboard")

    context = {
        'form': form
    }
    return render(request, 'add.html', context)

@login_required(login_url='login')
def postsDashboardPage(request):

    totalPosts = Post.objects.filter(user=request.user)

    context = {
        'posts':totalPosts,
    }
    return render(request, 'posts.html', context)


@login_required(login_url='login')
def deleteDashboardPostPage(request, id):
    post = Post.objects.get(id=id)
    user = User.objects.get(username=request.user)
    if post.user == user:
        post.delete()
        return redirect('dashboard')

@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        message = "Couldn't Authenticate, Either User Or Password Wrong."
        context = {"message": message}
        return render(request, 'public/login.html', context)

    context = {}
    return render(request, 'public/login.html', context)

@unauthenticated_user
def signUpPage(request):
    form = CreateUserForm()
    
    if request.method == 'POST':
        try:
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
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

    # manga, anime, webtoon, manhwa

    manga = Post.objects.filter(Q(user=user) & Q(type="Manga")).count()
    anime = Post.objects.filter(Q(user=user) & Q(type="Anime")).count()
    manhwa = Post.objects.filter(Q(user=user) & Q(type="Manhwa")).count()
    webtoon = Post.objects.filter(Q(user=user) & Q(type="Webtoon")).count()

    context = {
        "user": user,
        "posts": userPosts,
        "postsT": userPostsT,
        'manga':manga,
        'anime':anime,
        'manhwa':manhwa,
        'webtoon':webtoon
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
