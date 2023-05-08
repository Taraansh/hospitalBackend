from django.urls import path
from patients import views

urlpatterns = [
    path('profile/<str:email>/<str:password>/', views.profile, name="profile"),
    path('modify/<str:email>/<str:password>/', views.modify, name="modify"),
    path('loginreq/<str:email>/<str:password>/', views.loginreq, name="loginreq"),
    path('signup/', views.signup, name='signup'),
]
