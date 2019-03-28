# mobile-app-version-checker
A django app module to check/update mobile apps(ios/android) version.


## Initial Endpoints
Only a superadmin has the privilege to list/update the mobile versions.
- List mobile versions: GET request method
```
mobile-version
```
- Update mobile versions: PUT request method
```
mobile-version/<int:pk>
```
Version Check
```
check-version/
```


## Requirements
- Django: https://www.djangoproject.com/download/
```
$ pip install django
```

- Django Rest Framework: https://www.django-rest-framework.org/#installation
```
$ pip install djangorestframework
```


### Optional Requirements 
- django-rest-auth: This library provides a set of REST API endpoints for registration, authentication (including social media authentication), password reset, retrieve and update user details, etc. By having these API endpoints, your client apps such as AngularJS, iOS, Android, and others can communicate to your Django backend site independently via REST APIs for user management.
```
$ pip install django-rest-auth
```


## Add followings to settings.py
```
INSTALLED_APP = [
	...
	'rest_framework',
	'rest_framework.authtoken', # required if used django rest framework's Token Authentication
	
	'mobile_version_app',
	...
]


\# Codes for API response
ERROR_CODE = 0
SUCCESS_CODE = 1 
APP_UPDATE_MANDATORY = 4 
APP_UPDATE_OPTIONAL = 5

```


## Initial Setups
- Migrate the models
```
$ python manage.py migrate mobile_version_app
```

- Load the initial data for mobile app versions. Initial data can be updated in file `/mobile_version_app/management/commands/load_data.py`
```
$ python manage.py load_data
```


## Add followings to urls.py
```
urlpatterns = [
	...
	path('', include('mobile_version_app.urls))
]
```
