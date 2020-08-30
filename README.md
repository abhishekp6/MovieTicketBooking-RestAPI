  # Movie Ticket Booking System - RestAPI
    

    
### Description

The Rest API supports following business cases
    - An endpoint to book a ticket using a user’s name, phone number, and timings  
    - An endpoint to update a ticket timing
    - An endpoint to view all the tickets for a particular time
    - An endpoint to delete a particular ticket
    - An endpoint to view the user’s details based on the ticket id

### Prerequisites

What things you need to install the software and how to install them
- Code Editor(Visual Studio Preferred)</br>
- Python 3+ installed globally on the system
- Pip installed
- Virtual environment installed
- Ubuntu 18.04
 
### Installing

Step 1: git clone https://github.com/abhishekp6/MovieTicketBooking-RestAPI.git

Step 2: cd into your the cloned repo as such:

        $ cd MovieTicketBooking-RestAPI

Step 3: Create and fire up your virtual environment:

        $ virtualenv venv -p python3
        $ source venv/bin/activate

Step 4: Install the dependencies needed to run the app:

        $ pip install django
        $ pip install djangorestframework
        

Step 5: Make those migrations work

        $ python manage.py makemigrations
        $ python manage.py migrate

Run It

Fire up the server using this one simple command:

    $ python manage.py runserver

You can now access the file api service on your browser by using

    http://localhost:8000/api/bookticket
    http://localhost:8000/api/updatetime
    http://localhost:8000/api/viewticket
    http://localhost:8000/api/viewuser
    http://localhost:8000/api/deleteticket


## Testing Screenshots of Postman (DEMO)
![](https://github.com/abhishekp6/MovieTicketBooking-RestAPI/blob/master/static/1%20(copy).png)
![](https://github.com/abhishekp6/MovieTicketBooking-RestAPI/blob/master/static/2%20(copy).png)
![](https://github.com/abhishekp6/MovieTicketBooking-RestAPI/blob/master/static/3%20(copy).png)
![](https://github.com/abhishekp6/MovieTicketBooking-RestAPI/blob/master/static/4%20(copy).png)
![](https://github.com/abhishekp6/MovieTicketBooking-RestAPI/blob/master/static/5%20(copy).png)

## Built With

* [Django](https://docs.djangoproject.com/en/3.1/) - The web framework used
* [Django REST framework](https://www.django-rest-framework.org/) - The Web framework used 

## Authors

* **Abhishek Pandey** 
