from django.urls import path
from appointment import views

urlpatterns = [
    path('myappointment/<str:patient_email>/', views.appointment_list, name='appointment_list'),
    path('book/<str:patient_email>/', views.book_appointment, name='book_appointment'),
    path('upcoming/<str:doctor>/', views.upcoming_appointments, name='upcoming_appointments'),
]
