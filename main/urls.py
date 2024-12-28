from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('hr/', views.hr, name='hr'),
    path('payroll/', views.payroll, name='payroll'),
    path('assignment/', views.assignment, name='assignment'),
    path('jobs/', views.jobs, name='jobs'),
    path('recruitment/', views.recruitment, name='recruitment'),
    path('usersmanagement/', views.usersmanagement, name='usersmanagement'),

    path('newassignment', views.newassignment, name='newassignment'),
]
