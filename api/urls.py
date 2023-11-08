
from django.urls import path
from api import views



urlpatterns = [
    path('auth/authorize/', views.authview.OAuthAuthorizeView.as_view(), name='oauth-authorize'),
    path('auth/callback/', views.authview.oauth2_callback.as_view(), name='oauth-callback'),
    path('api/users/', views.userviews.UserList.as_view(),),
    path('api/user/<int:user_id>/', views.userviews.UserDetailView.as_view(), name='user-detail'),
    path('get_user_data/', views.authview.GetUserDataView.as_view(), name='get_user_data'),
    path('api/projects/', views.projectviews.ProjectList.as_view(),),
    path('api/project/<int:project_id>/', views.projectviews.ProjectDetailView.as_view(), name='project-detail'),
    path('api/user/<int:user_id>/projects/', views.projectviews.UserProjectListView.as_view(), name='user-projects-list'),
    path('api/create_project/', views.projectviews.CreateProjectView.as_view(), name='create_project'),
    path('api/project/<int:project_id>/lists/', views.listview.Listslist.as_view(), name='lists-list'),
    path('api/lists/<int:list_id>/', views.listview.ListsDetail.as_view(), name='lists-detail'),
    path('add-member/', views.memberview.ProjectMembersCreateView.as_view(), name='add-member'),
    path('project-members/<int:project_id>/', views.memberview.ProjectMembersListView.as_view(), name='project-members'),
]
