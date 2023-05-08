from django.urls import path
from otherusers import views

urlpatterns = [
    path('loginreq/<str:email>/<str:password>/', views.loginreq, name="loginreq"),
    path('modify/<str:email>/<str:password>/', views.modify_availability, name="modify_availability"),
    path('profile/<str:email>/<str:password>/', views.profile, name="profile"),
    path('otheruser/<str:email>/<str:password>/', views.otheruser_login, name="otheruser_login"),
    path('otherprofile/<str:email>/<str:password>/', views.other_profile, name="other_profile"),
    path('doctors/', views.doctors_list, name="doctors_list"),
]
