from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework import permissions, status, generics
from rest_framework.response import Response

from core.utils import CustomJSONWebTokenAuthentication
from core.serializers import UserSerializer
# Create your views here.
class IndeeUserGroupSetPagination(PageNumberPagination):
    """
    When we override the get, querystring pagination breaks and doesnt work.
    Also customizatized pagination with ProjectListResultsSetPagination.
    http://stackoverflow.com/questions/36636233/django-rest-framework-3-2-3-pagination-not-working-for-generics-listcreateapivie
    https://github.com/tomchristie/django-rest-framework/blob/master/rest_framework/mixins.py#L39
    """
    page_size = 9
    page_size_query_param = 'limit'
    max_page_size = 30

class UsersList(APIView):
    """
    API Endpoint for list of users , doesnt need token for POST(not implemented yet), GET only for staff.
    """
    authentication_classes = (JSONWebTokenAuthentication,)
    #permission_classes = (permissions.IsAdminUser,)
    permission_classes = (permissions.AllowAny,)
    model = User
    #throttle_classes = (AnonymousRateThrottle,)

    def get_permissions(self):
        """
        Override the permissions for POST
        """
        if self.request.method == 'POST':
            self.permission_classes = (permissions.AllowAny,)
        return super(UsersList, self).get_permissions()

    def get_queryset(self, request):
        """
        API Endpoint to get user list , only allowed for staff.
        """
        if request.user.is_staff:
            user_list = User.objects.all()
            return user_list
        else:
            return None

    def get(self, request):
        """
        Return user details.
        """
        import pdb;pdb.set_trace()
        try:
            queryset = self.get_queryset(request)
            serializer = UserSerializer(queryset, many=True)
            return Response(serializer.data)
        except Exception as get_user_list_error:
            return Response(
                {
                    'message': 'Your request could not be processed. Please try again after some time.',
                    'error':str(get_user_list_error)
                },
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request):
        return Response(
            {
                "message": "PUT method not allowed",
                "error": True,
            },
            status=status.HTTP_405_METHOD_NOT_ALLOWED
        )

    def delete(self, request):
        return Response(
            {
                "message": "DELETE method not allowed",
                "error": True,
            },
            status=status.HTTP_405_METHOD_NOT_ALLOWED
        )

