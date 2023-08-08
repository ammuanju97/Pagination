

from django.urls import path
from .views import  PostList

from .views import Index
 
urlpatterns = [
    path('', Index),
    path('', PostList.as_view())
   
 
]