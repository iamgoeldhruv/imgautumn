
from django.urls import path
from . import views


urlpatterns = [
    path('auth/authorize/', views.OAuthAuthorizeView.as_view(), name='oauth-authorize'),
    path('auth/callback/', views.oauth2_callback.as_view(), name='oauth-callback'),
    path('api/users/', views.UserList.as_view(),),
    path('api/user/<int:user_id>/', views.UserDetailView.as_view(), name='user-detail'),
    path('get_user_data/', views.GetUserDataView.as_view(), name='get_user_data'),

] 