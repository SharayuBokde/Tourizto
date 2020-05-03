from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Blog, Image
from .forms import BlogForm
from django.forms import modelformset_factory

# Create your views here.
def travelouge(request):
    blogs = Blog.objects.all().order_by('-time_stamp')
    context = {'blogs':blogs, 'title':'Travelouge'}
    return render(request, 'travelouge.html', context)

def new_blog(request):
    ImageFormset = modelformset_factory(Image, fields=('display_image',), extra=1)
    if request.method =="POST":
        form = BlogForm(request.POST, request.FILES)
        formset = ImageFormset(request.POST, request.FILES)
        if form.is_valid() and formset.is_valid():
            form_item = form.save(commit=False)
            form_item.author=request.user
            form_item.save()
            for f in formset:
                print(f.cleaned_data)
                try:
                    photo = Image(blog=form_item, image=f.cleaned_data['display_image'])
                    photo.save()
                except Exception as e:
                    break
            messages.success(request,"Blog created successfully")
            return redirect('travelouge')
    else:
        form = BlogForm()
        formset = ImageFormset(queryset=Image.objects.none())
    context = {'form':form, 'formset':formset}
    return render(request, 'add_blog.html', context) 

def view_blog(request, id):
    blog = Blog.objects.get(id=id)
    content = blog.content.split('#')
    context = {'blog':blog,'content':content,'title':'Blog'}
    return render(request, 'view_blog.html', context)

def like(request, id):
    blog = Blog.objects.get(id=id)
    user = request.user
    if user in blog.likes.all():
        blog.likes.remove(user)
        messages.info(request, 'You disliked the Blog.')
    else:
        blog.likes.add(user)
        messages.info(request, 'You liked the Blog.')
    return redirect('view_blog', id=id)

def update_blog(request, id):
    blog = Blog.objects.get(id=id)
    form = BlogForm(instance=blog)
    if request.method == 'POST':
        form = BlogForm(request.POST or None, request.FILES or None, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, 'The Blog has been updated successfully')
            return redirect('view_blog', id=id)
    context = {'form':form}
    return render(request, 'update_blog.html', context)

def delete_blog(request, id):
    blog = Blog.objects.get(id=id)
    blog.delete()
    messages.error(request, 'The Blog has been successfully deleted')
    return redirect('travelouge')
