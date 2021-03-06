
# MSC Final Year Project

In this project we made a management system for the Medical Store.
As the name suggest it manages record of the buying as well as selling 
the medicine. It saves and manages the record of medicine bought the
patient. It also keeps record of Dealer, Employee, Customer, Medicine
and Purchase.

To run this project in your system either copy requirements.txt file
by creating and activating virtual environment or just follow the steps given below.

Install django in your system using the following command:

> pip install Django==1.11.6

Current version is Django 2.0.9 but this project uses the older version.

You can make use of any text editor such as Sublime, Atom, Pycharm, Webstorm etc. The link for Pycharm is mentioned below: 
Download the community(free) version.
https://www.jetbrains.com/pycharm/download/#section=windows

Open Pycharm, open the extracted project folder in Pycharm.
Go to Pycharm terminal and enter the following command:
> python manage.py runserver

URL routing is handled in the file: pharma/urls.py

All the functionalities such as Create, update, delete, retrieve are present in the file: pharma/views.py

The database by default used with Django is SQLite3:

The database models are created in the file: pharma/models.py

Iff any changes are made in the models.py file such as adding, deleting fields or new tables, run the following two commands:

> python manage.py makemigrations pharma
> python manage.py migrate


All the SQL queries are generated by Django implicitly. You can view the SQL commands using the following command:

> python manage.py sqlmigrate pharma migration_name

"migration_name" is the file name generated during each Model file update, choose any filename from the folder and enter in the command to see the SQL commands of that update.