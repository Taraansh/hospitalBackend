from django.urls import path
from pharmacy import views

urlpatterns = [
    path('list/', views.medicine_list, name='medicine_list'),
    path('detail/<int:medicine_id>/', views.medicine_detail, name='medicine_detail')
]
