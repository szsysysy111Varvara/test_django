from django.urls import path
#from myapp.views import greeting
from myapp.views import hello_user

#urlpatterns = [
   #path('', greeting, name='greeting'),
#]


urlpatterns = [
    path('', hello_user, name='hello'),
]