# Simple app for your jokes.

An simple c.r.u.d app, that lets user to write, delete, and update their favorite jokes.
Users are not authenticated, and this is made just for testing purposes and learning in mind!

[Detailed report](https://github.com/therealhalonen/python_web_service/blob/master/pw3/report.md)

Screenshots:
Main page:

![Image 1](https://github.com/therealhalonen/python_web_service/blob/master/pw3/res/ss_main.png)

Detail view:

![Image 2](https://github.com/therealhalonen/python_web_service/blob/master/pw3/res/ss_details.png)

Editing details, in this case only origin can be edited from detail view:

![Image 1](https://github.com/therealhalonen/python_web_service/blob/master/pw3/res/ss_edit_detail.png)

Delete:

![Image 2](https://github.com/therealhalonen/python_web_service/blob/master/pw3/res/ss_delete.png)

Add new, same as edit, but in edit view, origin is not allowed on purpose:

![Image 1](https://github.com/therealhalonen/python_web_service/blob/master/pw3/res/ss_new.png)

New submitted:

![Image 2](https://github.com/therealhalonen/python_web_service/blob/master/pw3/res/ss_new_submitted.png)

**DO THIS ON A VIRTUAL MACHINE OR SOME PC YOU DONT HAVE ANY IMPORTANT STUFF**

Installation:
```
$ mkdir test_folder
$ cd test_folder
$ git init
$ git clone https://github.com/therealhalonen/django_test_jokes
$ sudo apt-get -y install virtualenv
$ virtualenv --system-site-packages -p python3 env/
$ source env/bin/activate
$ pip install -r requirements.txt
$ ./manage.py runserver
```
Go to http://127.0.0.1:8000/ with your browser. *firefox preferred*

**Profit!**
