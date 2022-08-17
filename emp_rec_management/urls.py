from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('employee_signup',views.employee_signup, name="employee_signup"),
    path('employee_login',views.employee_login, name="employee_login"),
    path('employee_signout',views.employee_signout, name="employee_signout"),
    path('dashboard',views.dashboard, name="dashboard"),
    path('emp_profile',views.emp_profile, name="emp_profile"),
    path('emp_edit_profile',views.emp_edit_profile, name="emp_edit_profile"),
    path('emp_experience',views.emp_experience, name="emp_experience"),
    path('emp_education',views.emp_education, name="emp_education"),

    


]
