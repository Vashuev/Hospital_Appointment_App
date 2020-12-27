from . import views
from django.urls import path

urlpatterns = [
    path('', views.homePage, name='home'),
    path('patient/', views.patientPage, name="patient"),

    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutPage, name="logout"),

    path('create_appointment/<str:pk>', views.create_appointment, name="create_appointment"),
    path('update_apoint/<str:pk>/', views.update_appointment, name="update_appoint"),
    path('delete_appoint/<str:pk>/', views.delete_appointment, name="delete_appoint"),

    path('prescription/<str:pk>', views.prescription, name="prescription"),
    path('appointment/<str:pk>/<str:time>', views.appointment, name="appointment"),
]
