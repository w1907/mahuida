from django.urls import path
from .views import *


urlpatterns = [
    path('', Index, name="index_mantenedor"),
    path('add_user', AddUsuarios, name="add_user"),
    path('list_user', ListUsuarios, name="list_user"),
    path('edit_user/<int:id>', EditarUsuarios, name="edit_user"),
    path('delete_user/<int:id>', EliminarUsuarios, name="delete_user")
]