from django.urls import path
from patients import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    # path('login/', views.login, name="login"),
    path('loginreq/<str:email>/<str:password>/', views.loginreq, name="loginreq"),
    path('modify/<str:email>/<str:password>/', views.modify, name="modify"),
    path('profile/<str:email>/<str:password>/', views.profile, name="profile"),
]
