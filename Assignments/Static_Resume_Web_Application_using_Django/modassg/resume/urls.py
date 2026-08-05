from django.urls import path
from .views import res

urlpatterns = [path('resume',res, name='resume'),]

