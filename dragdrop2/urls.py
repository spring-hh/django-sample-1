from django.urls import path
from . import views

urlpatterns = [
    path("", views.drapdrop2, name="drapdrop2"),
]
