from django.urls import path
from .views import login_view, register_student, register_teacher, index
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('login/', login_view, name="login"),
    path('', index, name="home"),
    path('register_student/', register_student, name="register_student"),
    path('register_teacher/', register_teacher, name="register_teacher"),
    path("logout/", views.logout, name="logout"),
    path("profile/", views.profile, name="profile"),
    path("all_details/", views.all_details, name="all_details"),
    path("edit/", views.edit, name="edit"),
    path("details/", views.details, name="details"),
    path("adharCard/", views.adharCardView, name="adhar card"),
    path('submit_timesheet/', views.submit_timesheet, name='submit_timesheet'),
]
