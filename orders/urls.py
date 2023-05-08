from orders import views
from django.urls import path

urlpatterns = [
    path('myorder/<str:patient_email>/', views.view_order_by_patient, name="view_order_by_patient"),
    path('order/<int:order_id>/delete/', views.delete_order, name="delete_order"),
    path('allorders/', views.all_orders, name="all_orders"),
    path('order/<int:order_id>/status/', views.modify_order_status, name='modify_order_status'),
    path('order/<str:patient_email>/', views.create_order, name="create_order"),
]