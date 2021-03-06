<br />
<p align="center">
  <img src="Tourizto Images/0brand.png" alt="Logo" height=50 width=auto>
  
  <p align="center">
    A web app that lets you book travel tickets according to your convenience!
    <br />
    <a href="https://github.com/SharayuBokde/Tourizto"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    View Demo
    ·
    <a href="https://github.com/SharayuBokde/Tourizto/issues">Report Bug</a>
    ·
    <a href="https://github.com/SharayuBokde/Tourizto/issues">Request Feature</a>
  </p>
</p>

## Install

Clone the repository
    
    git clone https://github.com/SharayuBokde/Tourizto.git
  
Create and activate the virtual environment
    
    virtualenv venv
    cd scripts
    activate
      
Navigate back to the main folder. Install the requirements and make migrations

    pip install -r requirements.txt
    python manage.gy makemigrations
    python manage.py migrate
    python manage.py runserver


## About the Project
Tourizto is a complete web package. Tourizto contains relevant package and services that are of a need to customers. Tourizto tours and travel has various packages which are basically services that our website provides. Best part is, Tourizto tours and travel is designed especially for customers who have no time to select and manage their holidays. Tourizto tours and travel saves a lot of time for its user by giving them detailed itinerary about the day-to-plan. Tourizto is a secured web application made using Django framework. India, one of the most beautiful locations of South Asia is also among popular countries of the world. Therefore this tourist hub welcomes more than a 5 million foreign tourist from different location of the world. A trip to this beautiful country can reveal numerous mystic things regarding its culture, art, tradition; history etc. known for its spectacular culture, India has become a favored place of visit for travelers from all over the world. Each state of this wonderful country is unique when it comes to the scenic beauty nature of the people living in the country and hospitality of Indians.

<h3 align="center"><img src="Tourizto Images/tourizto.gif" height=auto width=90%></h3>

## Built with 🔨
* Python3
* Django Web Framework
* Stripe for Payment
* Dialogflow for Chatbot
* Frontend: 
  * HTML
  * CSS
  * Bootstrap 
  * JavaScript
* PostgreSQL

## Pages

* Home - This page provides concise information about the features of the website. The navigation bar contains link to all the other section of the website. The main page displays recommendations with the best deals provided by the tours and Travel Company. Users can login into their accounts and benefit from a wide range of discounts provided by the website. Admin can add new itinerary by forms. This is explained in later under Admin.

* About - This page provides information about the development of the company and its operations.

* Contact - This page provides contact information like phone number, email-id etc., to the users.

* Itenierary - This page provides complete information of a desired destination. It provides the customer with overview, highlights, itinerary, estimated price and inquiry option. It also specifies all the terms and conditions. The admin at the same time can add, update and delete a place. To add a place the admin needs to enter information as specified in the model.
 
* Booking and Payment - Booking page requires the user to enter the details such as name email-id, phone number, residence area, arrival and departure dates, number of adults and children, accommodation and food preference details. These data are stored in the database. According to the data filled by the customer, total price is calculated by the system. Before proceeding for payment the user is redirected to next page where he/she can check the total price and other details. Then the user can finally proceed to the payment gateway. Payment page requires the user to enter the details of the credit card necessary to make an online payment. After successful payment, you are redirected to the page where you cant opt for a confirmation email. Once the payment and confirmation email is received you are then redirected to My Bookings page where you can view all you bookings from past.

* Travelouge - Travelouge is an addition feature in our website which provides the user with information about the different highlights of India. Blogs simply makes the selection process a bit simpler and efficient for the user. Admin needs to enter the images as well as description which are stored in the database. The user can view and like the blog. 

* Review - A review enables the user to share their travel experience with other users. User can refer to the review posted by other users in their booking process.

* Profile - This page displays the user’s profile which contains username, email, blogs posted by the user and reviews posted by the user.

* Chatbot - The purpose of this feature is to answer the queries faced the user during their booking process. It asks for basic details like name, destination for tour, arrival and departure dates, email address from where we will be able to communicate with the user for further procedures.

## Contributing 🤝
Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are greatly appreciated.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Developed with ❤️ by

**_Rutu Gaglani_** - [Github](https://github.com/rutugaglani) - Frontend & Graphic Design

**_Saurav Tiwari_** - [Github](https://github.com/sauravtiwari27) - Frontend & Graphic Design

**_Sharayu Bokde_** - [Github](https://github.com/SharayuBokde) - Full-stack & Database
