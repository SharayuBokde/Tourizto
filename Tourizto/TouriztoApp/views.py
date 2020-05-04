import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Destination, Images
from .forms import DestinationForm 
from django.forms import modelformset_factory
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    dests = Destination.objects.all().order_by('-id')
    context = {'dests':dests, 'title':'Home'}
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def chatbot(request):
    return render(request, 'chatbot.html')

def contact(request):
    context = {'title':'Contact'}
    return render(request, 'contact.html', context)

def new_itenary(request):
    ImageFormset = modelformset_factory(Images, fields=('image',), extra=6)
    if request.method =="POST":
        form = DestinationForm(request.POST, request.FILES)
        formset = ImageFormset(request.POST, request.FILES)
        if form.is_valid() and formset.is_valid():
            form_item = form.save(commit=False)
            form_item.save()
            for f in formset:
                print(f.cleaned_data)
                try:
                    photo = Images(destination=form_item, image=f.cleaned_data['image'])
                    photo.save()
                except Exception as e:
                    break
            messages.success(request,"Itenary created successfully")
            return redirect('home')
    else:
        form = DestinationForm()
        formset = ImageFormset(queryset=Images.objects.none())
    context = {'form':form, 'formset':formset}
    return render(request, 'add_itenary.html', context) 

def view_itenary(request, id):
    dest = Destination.objects.get(id=id)
    print(f'destination is {dest}')
    price = int(dest.price)
    if dest.offer:
        disc = int(dest.discount)
        discounted_rate =  price - (disc*price)/100
    description = dest.description.split('#')
    highlights = dest.highlights.split('#')
    itenary_titles = dest.itenary_titles.split('#')
    itenary = dest.itenary.split('#')
    itenary_list = zip(itenary_titles, itenary)
    context = {'dest':dest, 'discounted_rate':discounted_rate, 'highlights':highlights, 'itenary_list':itenary_list, 'description':description}
    return render(request, 'itenary.html', context)

def like(request, id):
    dest = Destination.objects.get(id=id)
    user = request.user
    if user in dest.likes.all():
        dest.likes.remove(user)
        messages.info(request, f'You disliked the Destination : {dest.name}')
    else:
        dest.likes.add(user)
        messages.info(request, f'You liked the Destination : {dest.name}')
    return redirect('view_itenary', id=id)

def update_itenary(request, id):
    dest = Destination.objects.get(id=id)
    form = DestinationForm(instance=dest)
    if request.method == 'POST':
        form = DestinationForm(request.POST or None, request.FILES or None, instance=dest)
        if form.is_valid():
            form.save()
            messages.success(request, 'The Destination has been updated successfully')
            return redirect('view_itenary', id=id)
    context = {'form':form}
    return render(request, 'update_itenary.html', context)

def delete_itenary(request, id):
    dest = Destination.objects.get(id=id)
    dest.delete()
    messages.error(request, f'The Destination : {dest.name} has been successfully deleted')
    return redirect('home')
