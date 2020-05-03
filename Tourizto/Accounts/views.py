from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from .forms import UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.models import User
from Travelouge.models import Blog
from Review.models import Review

# Create your views here.
def register(request):
    if request.method == 'POST':
        # Get user parameters
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        # Check for error
        if len(username) > 15 and len(username) < 3:
            messages.error(request, 'Username must be between 3 to 15 characters')
            return redirect('home')
        if not username.isalnum():
            messages.error(request, 'Username should only contain letters and numbers')
            return redirect('home')
        if password1 != password2:
            messages.error(request, 'Passwords do not match')
            return redirect('home')

        # Create the user
        myuser = User.objects.create_user(username, email, password1)
        myuser.first_name = firstname
        myuser.last_name = lastname
        myuser.save()
        messages.success(request, 'Your account has been successfully created')
        return redirect('home')
    else:
        return HttpResponse('Error 404 - Not Found')

def loginview(request):
    if request.method == 'POST':
        username = request.POST['loginusername']
        password = request.POST['loginpassword']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully Logged In')
            return redirect('home')
        else:
            messages.warning(request, 'Invalid Credentials')
            return redirect('home')
    else:
        return HttpResponse('Error 404 - Not Found')

def logoutview(request):
    logout(request)
    messages.success(request, 'Successfully Logged Out')
    return redirect('home')

@login_required
def profile(request):
    reviews = Review.objects.filter(author=request.user).order_by('-id')
    blogs = Blog.objects.filter(author=request.user).order_by('-id')
    review_count = Review.objects.filter(author=request.user).count()
    blog_count = Blog.objects.filter(author=request.user).count()
    context = {'reviews':reviews, 'blogs':blogs, 'blog_count':blog_count, 'review_count':review_count}
    return render(request, 'profile.html', context)

@login_required
def settings(request):
    if request.method == 'POST':
        userform = UserUpdateForm(request.POST, instance=request.user)
        profileform = ProfileUpdateForm(request.POST, request.FILES,instance=request.user.profile)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            profileform.save()
            messages.success(request, 'Your profile has been updated successfully')
            return redirect('profile')
    else:
        userform = UserUpdateForm(instance=request.user)
        profileform = ProfileUpdateForm(instance=request.user.profile)
    context = { 'userform':userform, 'profileform':profileform }
    return render(request, 'settings.html', context)








