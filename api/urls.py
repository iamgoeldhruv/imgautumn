
from django.urls import path
from api import views



urlpatterns = [
    path('auth/authorize/', views.authview.OAuthAuthorizeView.as_view(), name='oauth-authorize'),
    path('auth/callback/', views.authview.oauth2_callback.as_view(), name='oauth-callback'),
    path('api/users/<int:project_id>/', views.userviews.UserList.as_view(),),
    path('api/user/<int:user_id>/', views.userviews.UserDetailView.as_view(), name='user-detail'),
    path('get_user_data/', views.authview.GetUserDataView.as_view(), name='get_user_data'),
    path('api/projects/', views.projectviews.ProjectList.as_view()),
    path('api/project/<int:project_id>/', views.projectviews.ProjectDetailView.as_view(), name='project-detail'),
    path('api/user/<int:user_id>/projects/', views.projectviews.UserProjectListView.as_view(), name='user-projects-list'),
    path('api/create_project/', views.projectviews.CreateProjectView.as_view(), name='create_project'),
   
    path('project-members/<int:project_id>/', views.memberview.ProjectMembersListView.as_view(), name='project-members'),
    path('api/lists/<int:project_id>/', views.listview.ListsInProjectView.as_view(), name='lists-in-project'),
    path('api/project/<int:project_id>/create_list/', views.listview.CreateListView.as_view(), name='create-list'),
    path('api/list/<int:list_id>/', views.listview.UpdateDeleteListView.as_view(), name='update-delete-list'),
    path('api/cards/<int:list_id>/<int:project_id>/',views.cardview.CardDetailsInListView.as_view(), name='card-list'),
    path('api/card/create/', views.cardview.CreateCardDetailsView.as_view(), name='card-create'),
    path('api/user-projects/<int:user_id>/', views.memberview.UserProjectsView.as_view(), name='user-projects'),
     path('api/add-member/', views.memberview.ProjectMembersCreateView.as_view(), name='add-member'),
]
