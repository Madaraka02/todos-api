How to run project on Ubuntu:
```
$ mkdir Carrot

$ cd Carrot
```
Create a virtual environment to install dependencies in and activate it:

```
$ virtualenv2  venv
$ source venv/bin/activate
```

```
 $ git clone https://github.com/Madaraka02/Auction-system.git
 or 
 $ git clone git@github.com:Madaraka02/todos-api.git or
 $ git clone  https://github.com/Madaraka02/todos-api.git

 $ cd todos-api
```

Then install the dependencies:
```
(venv)$ pip install -r requirements.txt
```
Once pip has finished downloading the dependencies:
```
(venv)$ python manage.py makemigrations
(venv)$ python manage.py migrate
(venv)$ python manage.py runserver
```


How to run project on windows:
```
$ mkdir Carrot

$ cd Carrot
```
Create a virtual environment to install dependencies in and activate it:

```
$ python -m venv env
$ env\Scripts\activate
```

```
 $ git clone https://github.com/Madaraka02/Auction-system.git
 or 
 $ git clone git@github.com:Madaraka02/todos-api.git or
 $ git clone  https://github.com/Madaraka02/todos-api.git

 $ cd todos-api
```

Then install the dependencies:
```
(env)$ pip install -r requirements.txt
```
Once pip has finished downloading the dependencies:
```
(env)$ python manage.py makemigrations
(env)$ python manage.py migrate
(env)$ python manage.py runserver
```