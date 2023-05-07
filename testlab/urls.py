from django.urls import path
from testlab import views

urlpatterns = [
    path('tests/', views.test_list, name='test_list'),
    path('bookedtests/', views.booked_tests, name='booked_tests'),
    path('mytests/<str:patient_email>/', views.view_tests_booked_by_patient, name='view_tests_booked_by_patient'),
    path('uploadtestresults/<int:test_id>/', views.upload_test_results, name='upload_test_results'),
    path('test/<str:patient_email>/', views.book_test, name="book_test"),

]
