from django.urls import path
from .views import createAuthor, listAuthor, editAuthor, deleteAuthor

urlpatterns = [
    path('create_author/', createAuthor, name='Create_Author'),
    path('list_author/', listAuthor, name='List_Author'),
    path('edit_author/<int:id>', editAuthor, name='Edit_Author'),
    path('delete_author/<int:id>', deleteAuthor, name='Delete_Author')
]
