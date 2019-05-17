from django.urls import path
from.import views

app_name ="hospital"

urlpatterns = [
    path('',views.index,name="index"),
    path('about',views.about,name="about"),
    path('contact',views.contact,name="contact"),
    path('appointment',views.appointment,name="appointment"),
    path('doctorprofile',views.doctorprofile,name="doctorprofile"),
    path('single',views.single,name="single"),
    path('gallery',views.gallery,name="gallery"),
    path('staffprofile',views.staffprofile,name="staffprofile"),
    path('user_register', views.user_register, name="user_register"),
    path('user_login', views.user_login, name="user_login"),
    path('user_logout', views.user_logout, name="user_logout"),
    path('user_welcome', views.user_welcome, name="user_welcome"),
    path('profile', views.profile, name="profile"),
    path('doctor1', views.doctor1, name="doctor1"),
    path('doctor2', views.doctor2, name="doctor2"),
    path('doctor3', views.doctor3, name="doctor3"),
    path('doctor4', views.doctor4, name="doctor4"),
    path('doctor5', views.doctor5, name="doctor5"),
    path('doctor6', views.doctor6, name="doctor6"),
    path('doctor7', views.doctor7, name="doctor7"),
    path('doctor8', views.doctor8, name="doctor8"),
    path('doctor9', views.doctor9, name="doctor9"),
    path('doctor10', views.doctor10, name="doctor10"),
    path('doctor11', views.doctor11, name="doctor11"),
    path('doctor12', views.doctor12, name="doctor12"),
    path('doctor13', views.doctor13, name="doctor13"),
    path('doctor14', views.doctor14, name="doctor14"),
    path('patientform', views.patientform, name="patientform"),
    path('auth', views.auth, name="auth"),
    path('authL', views.authL, name="authL"),
    path('authR', views.authR, name="authR"),
    path('thankyou', views.thankyou, name="thankyou"),
]