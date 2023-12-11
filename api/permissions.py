from rest_framework.permissions import BasePermission
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from api import models

class IsProjectMemberPermission(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            raise AuthenticationFailed(detail="User not authenticated")

        # Get project_id from the URL parameters or request data
        project_id = None

        if 'project_id' in view.kwargs:
            # If project_id is in the URL parameters
            project_id = view.kwargs['project_id']
        elif 'project' in request.data:
            # If project_id is in the request data
            project_id = request.data['project']

        if not project_id:
            # If project_id is not present, permission denied
            return False

        # Check if the user is a member of the project
        is_project_member = models.ProjectMembers.objects.filter(
            user=request.user, project=project_id
        ).exists()

        return is_project_member
