# Simple app for your jokes.

An simple c.r.u.d app, that lets user to write, delete, and update their favorite jokes.
Users are not authenticated, and this is made just for testing purposes and learning in mind!

[Detailed report](https://github.com/therealhalonen/python_web_service/blob/master/pw3/report.md)

Screenshots:

![Image 1](/pw3/res/ss_main.png)
![Image 2](/pw3/res/ss_details.png)
![Image 1](/pw3/res/ss_edit_detail.png)
![Image 2](/pw3/res/ss_delete.png)
![Image 1](/pw3/res/ss_new.png)
![Image 2](/pw3/res/ss_new_submitted.png)

**DO THIS ON A VIRTUAL MACHINE OR SOME PC YOU DONT HAVE ANY IMPORTANT STUFF**

Installation:
```
$ mkdir test_folder
$ cd test_folder
$ git init
$ git pull https://github.com/therealhalonen/django_test_jokes
$ sudo apt-get -y install virtualenv
$ virtualenv --system-site-packages -p python3 env/
$ source env/bin/activate
$ pip install -r requirements.txt
$ ./manage.py runserver
```
Go to http://127.0.0.1:8000/ with your browser. *firefox preferred*
**Profit!**
