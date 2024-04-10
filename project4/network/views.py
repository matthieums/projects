from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django import forms
from django.utils import timezone
from django.contrib.auth.decorators import login_required
import json

from .forms import PostForm
from .models import User, Post


def index(request):
    if request.method == 'GET':
        user = request.user
        postform = PostForm()
        posts = Post.objects.order_by("-creation_date", "-creation_time")  
        return render(request, "network/index.html",{
            "postform":postform,
            "recent_posts":posts,
            "user":user
        })
    
    if request.method == 'POST':
        form = PostForm(request.POST)
        user = request.user
        if form.is_valid():
            post_content = form.cleaned_data['content']
            post = Post(content=post_content,
                        user=user)
            post.save()
            return HttpResponseRedirect(reverse("index"))
        return render(request, "network/index.html", {
            'postform': form
        })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")


def profile(request, username):
    current_user = request.user
    profile = User.objects.get(username=username)
    posts = Post.objects.filter(user=profile).order_by("-creation_date")

    return render(request, "network/profile.html", {
        "username":username,
        "posts": posts,
        "profile":profile,
        "user":current_user
        
    })

@login_required
def user(request, username):
    current_user = request.user
    user = User.objects.get(username=username)
    if user:
        follows = [user.username for user in current_user.follows.all()]
        
        data = {
            "follows" : follows
        }
        return JsonResponse(data)