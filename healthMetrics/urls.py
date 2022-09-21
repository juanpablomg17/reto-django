from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registeruser/', views.registerUser),
    path('editingUser/<id>', views.editingUser),
    path('editUser/<id>', views.editUser),
    path('deleteUser/<id>', views.deleteUser),
]