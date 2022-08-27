from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_snippet, name='list_snippet'),
    path('snippets/<int:pk>', views.detail_snippet, name='detail_snippet'),
    path('snippets/new', views.create_snippet, name='create_snippet')
]
