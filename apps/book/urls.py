from django.urls import path
from .views import createAuthor

urlpatterns = [
    path('create_author', createAuthor, name='Create_Author')
]
