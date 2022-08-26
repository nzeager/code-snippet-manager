from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_snippets, name='list_snippets'),
]
