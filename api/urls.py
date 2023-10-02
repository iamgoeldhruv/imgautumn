
from django.urls import path
from . import views


urlpatterns = [
    path('api/users/', views.UserList.as_view(),),
    path('api/user/<int:user_id>/', views.UserDetailView.as_view(), name='user-detail'),

] 