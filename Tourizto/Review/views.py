from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Review
from .forms import ReviewForm

# Create your views here.
def experience(request):
    reviews = Review.objects.all().order_by('-time_stamp')
    context = {'reviews':reviews, 'title':'Experience'}
    return render(request, 'experience.html', context)

def new_review(request):
    if request.method =="POST":
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form_item = form.save(commit=False)
            form_item.author=request.user
            form_item.save()
            messages.success(request,"Your Review created successfully")
            return redirect('experience')
    else:
        form = ReviewForm()
    context = {'form':form}
    return render(request, 'add_review.html', context) 

def view_review(request, id):
    review = Review.objects.get(id=id)
    content = review.content.split('#')
    context = {'review':review,'content':content,'title':'Review'}
    return render(request, 'view_review.html', context)

def like(request, id):
    review = Review.objects.get(id=id)
    user = request.user
    if user in review.likes.all():
        review.likes.remove(user)
        messages.info(request, 'You disliked the Review.')
    else:
        review.likes.add(user)
        messages.info(request, 'You liked the Review.')
    return redirect('view_review', id=id)

def update_review(request, id):
    review = Review.objects.get(id=id)
    form = ReviewForm(instance=review)
    if request.method == 'POST':
        form = ReviewForm(request.POST or None, request.FILES or None, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'The Review has been updated successfully')
            return redirect('view_review', id=id)
    context = {'form':form}
    return render(request, 'update_review.html', context)

def delete_review(request, id):
    review = Review.objects.get(id=id)
    review.delete()
    messages.error(request, 'The Review has been successfully deleted')
    return redirect('experience')
