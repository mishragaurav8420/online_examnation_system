from django.contrib import admin
from django.urls import path
from ots.views import *

urlpatterns = [
    path('', welcome),
    path('new-candidate',candidateRegistrationForm),
    path('store-candiate',candidateRegistration),
    path('login',loginView),
    path('home',candidateHome),
    path('test-paper',testPaper),
    path('calculate-result',calculateTestResult),
    path('test-history',testResultHistory),
    path('result',showTestResult),
    path('logout',logoutView),
    
]