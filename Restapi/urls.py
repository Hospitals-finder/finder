from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from Restapi import views
    


urlpatterns = [
    path('data/', views.HospitalsList.as_view()),
    path('data/<str:pincode>', views.HospitalsList.as_view())
]
urlpatterns=format_suffix_patterns(urlpatterns)
