from django.urls import path
from appointment import views

urlpatterns = [
    path('myappointment/<str:patient_email>/', views.appointment_list, name='appointment_list'),
    path('book/<str:patient_email>/', views.book_appointment, name='book_appointment'),


    path('appointments/<int:pk>/', views.appointment_detail, name='appointment_detail'),
    path('appointments/upcoming/', views.upcoming_appointments, name='upcoming_appointments'),
    path('appointments/doctor/', views.doctor_appointments, name='doctor_appointments'),
    path('appointments/update/', views.update_appointment, name='update_appointment'),
    path('availability/', views.doctor_availability, name='doctor_availability'),
]
