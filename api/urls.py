from django.urls import path
from . import views

urlpatterns = [
    path('docs/', views.api_docs, name='api_docs'),
    path('users/', views.get_users, name='get_users'),
    path('users/submit/', views.submit_user, name='submit_user'),
]
