from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('list/',employee_list,name='employee_list'),
    path('create/',employee_create,name='employee_create'),
    path('<int:pk>/edit/',employee_update,name='employee_update'),
    path('<int:pk>/delete/',employee_delete,name='employee_delete'),
    path('register/',register,name='register'),
    path('',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    
]
