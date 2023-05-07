from orders import views
from django.urls import path

urlpatterns = [
    path('order/<str:patient_email>/', views.create_order, name="create_order"),
    path('order/<int:order_id>/', views.view_order, name="view_order"),
    path('order/<int:order_id>/update/', views.update_order, name="update_order"),
    path('order/<int:order_id>/delete/', views.delete_order, name="delete_order"),
    path('order/<int:order_id>/status/', views.modify_order_status, name='modify_order_status'),
    path('myorder/<str:patient_email>/', views.view_order_by_patient, name="view_order_by_patient"),
    path('allorders/', views.all_orders, name="all_orders"),
]