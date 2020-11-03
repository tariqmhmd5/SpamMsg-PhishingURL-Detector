from django.urls import path
from home import views

urlpatterns = [
    path('',views.home),
    path('classify',views.classify),
    path('detectmessage',views.spam,name="spam"),
]