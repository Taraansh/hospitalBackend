from django.urls import path
from otherusers import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('loginreq/<str:email>/<str:password>/', views.loginreq, name="loginreq"),
    path('modify/<str:email>/<str:password>/', views.modify, name="modify"),
    path('profile/<str:email>/<str:password>/', views.profile, name="profile"),
    path('doctors/', views.doctors_list, name="doctors_list"),
    path('otheruser/<str:email>/<str:password>/', views.otheruser_login, name="otheruser_login"),
]
