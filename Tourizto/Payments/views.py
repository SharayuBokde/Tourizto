import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.core.mail import send_mail
from django.shortcuts import render,redirect
from django.contrib import messages
from django.urls import reverse
from django.http import JsonResponse
import stripe
from .models import Booking
from .forms import BookingForm
from TouriztoApp.models import Destination

stripe.api_key = "paste your api key here"

# Create your views here.
def mybookings(request):
    mybookings = Booking.objects.filter(customer_name=request.user).order_by('-timestamp')
    context = {'mybookings':mybookings}
    return render(request, 'mybookings.html', context)

def booking(request, id):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form_item = form.save(commit=False)
            form_item.customer_name = request.user
            form_item.customer_email = request.user.email
            form_item.destination = Destination.objects.get(id=id)
            adults = int(form_item.number_of_adults)
            children = int(form_item.number_of_children)
            price = int(form_item.destination.price)
            if form_item.destination.offer:
                discount = int(form_item.destination.discount)
                price = price - ((discount/100)*price)
            amount = ((0.75*children + adults)*price)
            form_item.total_price = amount
            form_item.save()
            messages.success(request,f"Payment for booking of INR {amount} has been initiated")
            return redirect('checkout', id=form_item.id)
    else:
        form = BookingForm()
    context = {'form':form}
    return render(request, 'booking.html', context)

def checkout(request, id):
    booking = Booking.objects.get(id=id)
    context = {'booking':booking}
    return render(request, 'checkout.html', context)

def cart(request, id):
    booking = Booking.objects.get(id=id)
    context = {'booking':booking}
    return render(request,'cart.html', context)

def charge(request, id):
    booking = Booking.objects.get(id=id)
    amount = booking.total_price
    if request.method == 'POST':
        print('Data: ' ,request.POST)
        customer=stripe.Customer.create(
            email=request.POST['email'],
            name=request.POST['name'],
            source=request.POST['stripeToken'],
        )
        charge= stripe.Charge.create(
            customer=customer,
            amount=amount*100,
            currency='inr',
            description="payment"
        )
    return redirect(reverse('success', args=[id]))

def successMsg(request, id):
   booking = Booking.objects.get(id=id)
   context = {'booking':booking}
   return render(request, 'success.html', context)

def confirmation_mail(request, id):
    if request.user.is_authenticated:
        booking = Booking.objects.get(id=id)
        name = booking.destination.name
        customer_name = booking.customer_name
        mail_content = f"""\
        <html>
        <body>
            <h3>Hello {customer_name}</h3>
            <p> Thankyou for purchasing a Travel Package from Tourizto! Your Payment for Booking {name} has been received.</p>
            <br>
            <table>
                <tr>
                    <th>Destination</th>
                    <th>{booking.destination.name}</th>
                </tr>
                <tr>
                    <td>Number of Adults</td>
                    <td>{booking.number_of_adults}</td>
                </tr>
                <tr>
                    <td>Number of Children</td>
                    <td>{booking.number_of_children}</td>
                </tr>
                <tr>
                    <td>Accomodation</td>
                    <td>{booking.accommodation}</td>
                </tr>
                <tr>
                    <td>Total Price</td>
                    <td>INR {booking.total_price}</td>
                </tr>
                <tr>
                    <td>Departute Date</td>
                    <td>{booking.departure_date}</td>
                </tr>
                <tr>
                    <td>Arrival Date</td>
                    <td>{booking.arrival_date}</td>
                </tr>
                <tr>
                    <td>Booked on</td>
                    <td>{booking.timestamp}</td>
                </tr>
            </table>
            <br>
            <p>We are very much pleased to serve you.</p>
            <br>
            <p>We wish you a Happy and Safe Journey!</p>
        </body>
        </html>
        """
        #The mail addresses and password
        sender_address = '_Enter senders email address_'
        sender_pass = '_Enter password for email provided in sender_address_'
        receiver_address = booking.customer_email
    
        #Setup the MIME
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        
        #The subject line
        message['Subject'] = f'Thankyou for your Order : {name} from Tourizto'
        
        #The body and the attachments for the mail
        message.attach(MIMEText(mail_content, 'html'))
        
        #Create SMTP session for sending the mail
        #use gmail with port
        session = smtplib.SMTP('smtp.gmail.com', 587) 
        #enable security
        session.starttls()
        #login with mail_id and password
        session.login(sender_address, sender_pass) 
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        
        messages.success(request, f'Thankyou for ordering from Travello.com to {name}')
        return redirect('mybookings')
    else:
        return redirect('home')
