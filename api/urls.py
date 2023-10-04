
from django.urls import path
from . import views


urlpatterns = [
    path('auth/authorize/', views.OAuthAuthorizeView.as_view(), name='oauth-authorize'),
    path('auth/callback/', views.oauth2_callback.as_view(), name='oauth-callback'),
    path('api/users/', views.UserList.as_view(),),
    path('api/user/<int:user_id>/', views.UserDetailView.as_view(), name='user-detail'),
    path('get_user_data/', views.GetUserDataView.as_view(), name='get_user_data'),
    path('api/projects/', views.ProjectList.as_view(),),
    path('api/project/<int:project_id>/', views.ProjectDetailView.as_view(), name='project-detail'),
    path('api/user/<int:user_id>/projects/', views.UserProjectListView.as_view(), name='user-projects-list'),

] 