from django.urls import path
from .views import *


urlpatterns = [
    path('', exchange),
    path('prog', prog)


]