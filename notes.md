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

(studentsdb)$ python manage.py shell

stud = Student(first_name="Vitaliy", last_name="Podoba", birthday=timezone.now(), ticket="234")