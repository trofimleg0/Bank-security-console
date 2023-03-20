# Bank security console #

A repository with a website for the course "Writing a Bank guard console" dvmn.org.  

This is an internal storage for a bank employee connected to a remote database.  If you got into this repository by accident, then you will not be able to run it without access to the database, but you can freely use the layout code or see how database queries are implemented.  

The site allows you to view the list of visits to the repository, the list of visitors at the moment, the number of employees with active passes and information about them.  

### How to install ### 

Python should be already installed.  

Copy the repository and go to the created directory
```commandline
git clone https://github.com/vitaliy-pavlenko/django-orm-watching-storage.git
```

Use `pip`(or `pip3` for Python3) to install dependencies:
```commandline
pip3 install -r requirements.txt
```
Recommended using [virtualenv/venv](https://docs.python.org/3/library/venv.html)

## Launch ##

Create .env file and add the configurations:
  - DB_SETTINGS=postgres://USER:PASSWORD@HOST:PORT/NAME
  - SECRET_KEY=your key
  - DEBUG=True/False
  - ALLOWED_HOSTS=['host1', 'host2']
  
Run `manage.py`
```commandline
python manage.py runserver 8000
```
## Project goals

The code is written for educational purposes — this is a lesson in a course on Python and web development on the [Devman](https://dvmn.org ).
