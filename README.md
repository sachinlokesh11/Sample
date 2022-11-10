
### Steps for Setup 
* install virtualenv using this command`python3 -m venv`
* activate virtualenv
* install requirements using this command `pip install -r requirements.txt`
* Run migration `python manage.py migrate`
* Run server `python manage.py runserver`
* Create User `python manage.py createsuperuser`
   * create your own user
   * add data to User Model here `http://127.0.0.1:8000/admin/users_app/usersmodel/`
   * sample data `{"id":1,"email":"george.bluth@reqres.in","first_name":"George","last_name":"Bluth","avatar":"https://reqres.in/img/faces/1-image.jpg"}`
  

### Test API
* http://127.0.0.1:8000/api/users/1
* http://127.0.0.1:8000/api/users/2
* http://127.0.0.1:8000/api/users/3
* http://127.0.0.1:8000/api/users