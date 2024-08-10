from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_world, name='hello_world'),  
    path('login/', views.login_view, name='login'),  
    path('signup/', views.signup_view, name='signup'),
    path('users/', views.get_all_users, name='get_all_users'),
    path('user/<str:email>/', views.get_user_by_email, name='get_user_by_email'),
    path('user/update/<str:email>/', views.update_user_details, name='update_user_details'),
    path('user/delete/<str:email>/', views.delete_user, name='delete_user'),
]
