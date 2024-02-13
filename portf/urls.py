from django.urls import path
from .views import *
from django.views.generic import RedirectView

urlpatterns = [
    path('', exchange),
    path('prog', prog),
    path('explanation', explanation),
    path('kp', kp),
    path('set_language/', RedirectView.as_view(url='/'), name='set_language'),


]