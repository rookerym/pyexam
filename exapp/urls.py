from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create_user', views.register),
    path('success', views.success),
    path('login_user', views.login),
    path('logout', views.logout),
    path('create_quote', views.create_quote),
    path('get_user/<int:user_id>', views.get_user),
    path('edit_user/<int:user_id>', views.edit_user),
    path('user/<int:user_id>', views.user_page),
    path('delete_quote/<int:post_id>', views.delete_quote),
]