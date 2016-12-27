3 $ mkdir -p /data/work/virtualenvs
6 $ cd /data/work/virtualenvs
11 $ virtualenv studentsdb --no-site-packages
20 $ cd studentsdb
26 $ source bin/activate
30 (studentsdb)$
35 $ which python
36 (studentsdb)$ which python
37 /data/work/virtualenvs/studentsdb/bin/python
38 (studentsdb)$ which pip
39 /data/work/virtualenvs/studentsdb/bin/pip

2 $ pwd
3 /data/work/virtualenvs/studentsdb
6 $ mkdir src
7 $cd src
14 $ ../bin/django-admin startproject studentsdb

### Running ###

$ cd proj/virtualenvs/studentsdb
$ source bin/activate
(studentsdb)$ cd scr/studentsdb
(studentsdb)$ python manage.py runserver
Performing system checks...
System check identified no issues (0 silenced).
November 01, 2014 - 13:01:39
Django version 1.7.1, using settings ’studentsdb.settings’
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.