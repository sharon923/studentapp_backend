from django.urls import path,include
from . import views

urlpatterns = [
    path('viewAll/', views.viewAll, name="viewAll"),
    path('add/', views.addStudent, name='add'),
    path('search/', views.searchStudent, name="search"),
    path('delete/', views.deleteStudent, name='delete')
    
]