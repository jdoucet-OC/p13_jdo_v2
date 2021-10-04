from django.urls import path, include
from .views import index

urlpatterns = [
    path('', include('lettings_address.urls')),
    path('', include('profiles.urls')),
    path('home/', index, name='index'),
]