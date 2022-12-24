from django.urls import path
from . import views


urlpatterns = [
    path('',views.Home,name='Home'),
    path('<int:id>',views.Update,name='Update')  ,
    path('delete/<int:id>', views.delete, name="delete")  
]
