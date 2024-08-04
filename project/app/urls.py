from django.urls import path
from .views import *

urlpatterns = [
     path('',home, name='home'), 
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('add_restaurant/', add_restaurant, name='add_restaurant'),
    path('restaurant/<int:id>/', restaurant_detail, name='restaurant_detail'),
    path('restaurant/<int:id>/add_review/', add_review, name='add_review'),
     # This is an API Urls
    path('api/restaurants/', RestaurantListCreate.as_view(), name='api_restaurants'),
    path('api/reviews/', ReviewListCreate.as_view(), name='api_reviews'),
]
