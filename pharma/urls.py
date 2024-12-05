from django.urls import path
from pharma.views import *

app_name='pharma'

urlpatterns=[
    path('tablets/',tablets,name='tablets'),
]