from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('',views.feedback_form, name='feedback_form')
]