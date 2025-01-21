from django.urls import path
from . import views

urlpatterns = [
    path('',views.form),
    path('ajax_HW3_1/',views.ajax_HW3_1),
]