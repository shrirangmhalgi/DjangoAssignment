from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse, HttpResponseNotAllowed, HttpResponseBadRequest
from .models import UserDetails
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import make_password, check_password
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
# hello world view
def hello_world(request):
    return HttpResponse("Hello, world!")

# Signup view
def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = make_password(request.POST['password'])  
        
        # Check if the email or username already exists
        if UserDetails.objects.filter(username=username).exists():
            return HttpResponse("Username already exists.")
        elif UserDetails.objects.filter(email=email).exists():
            return HttpResponse("Email already exists.")
        else:
            # Create a new user
            UserDetails.objects.create(username=username, email=email, password=password)
            return redirect('login')  
    return render(request, 'loginify/signup.html')

# Login view
def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = UserDetails.objects.filter(email=email).first()

        # Check if the user exists and the password is correct
        if user is not None and check_password(password, user.password):
            return render(request, 'loginify/success.html', {'username': user.username})  
        else:
            return HttpResponse("Invalid email or password.")
    
    return render(request, 'loginify/login.html')

# get all user details
def get_all_users(request):
    users = UserDetails.objects.all().values()
    return JsonResponse(list(users), safe=False)  # Convert QuerySet to a list

# get a single user by email
def get_user_by_email(request, email):
    user = get_object_or_404(UserDetails, email=email)
    return JsonResponse({
        'username': user.username,
        'email': user.email
    })

# update user details
@csrf_exempt
def update_user_details(request, email):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user = get_object_or_404(UserDetails, email=email)
            
            user.username = data.get('username', user.username)
            
            if 'password' in data:
                user.password = make_password(data['password'])  # Hash the password
            
            user.save()
            return JsonResponse({
                'message': 'User details updated successfully',
                'user': {
                    'username': user.username,
                    'email': user.email
                }
            })
        except json.JSONDecodeError:
            return HttpResponseBadRequest("Invalid JSON provided.")
    else:
        return HttpResponseNotAllowed(['POST'])  # Returns 405 Method Not Allowed for non-POST requests


# delete a user by email
@csrf_exempt
def delete_user(request, email):
    if request.method == 'DELETE':
        user = get_object_or_404(UserDetails, email=email)
        user.delete()
        return JsonResponse({'message': 'User deleted successfully'})
