# reviews/views.py
from django.contrib.auth import login, authenticate
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect,get_object_or_404, redirect
from.models import *
from .forms import *
from rest_framework import generics
from .serializers import RestaurantSerializer, ReviewSerializer

def home(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'home.html', {'restaurants': restaurants})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout(request):
    auth_logout(request)
    return redirect('home')


def add_restaurant(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RestaurantForm()
    return render(request, 'add-restaurent.html', {'form': form})

def restaurant_detail(request, id):
    restaurant = get_object_or_404(Restaurant, id=id)
    reviews = Review.objects.filter(restaurant=restaurant)
    return render(request, 'restaurant-detail.html', {'restaurant': restaurant, 'reviews': reviews})

@login_required(login_url='/signup/')  # Redirect to signup page if not logged in
def add_review(request, id):
    restaurant = get_object_or_404(Restaurant, id=id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.restaurant = restaurant
            review.user = request.user
            review.save()
            return redirect('restaurant_detail', id=restaurant.id)
    else:
        form = ReviewForm()
    return render(request, 'add-review.html', {'form': form})


# this is an API code 
class RestaurantListCreate(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class ReviewListCreate(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer