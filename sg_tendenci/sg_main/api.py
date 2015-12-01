from django.conf.urls import url, patterns, include
from django.contrib.auth.models import User, Group

from rest_framework import permissions, routers, serializers, viewsets
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route, api_view
from rest_framework.views import APIView
from rest_framework import authentication, permissions

from oauth2_provider.ext.rest_framework import TokenHasScope
from oauth2_provider.decorators import protected_resource

from oauth2_provider.ext.rest_framework import OAuth2Authentication, TokenHasScope

class WeakTokenHasSope(TokenHasScope):
    def has_permission(self, request, view):
        if request.successful_authenticator != OAuth2Authentication:
            return True
        return super().has_permission(request, view)

# first we define the serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')

#
# # ViewSets define the view behavior.
# class UserViewSet(viewsets.ModelViewSet):
#     permission_classes = [permissions.IsAuthenticated, TokenHasScope]
#     required_scopes = ['read']
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class UserView(APIView):
#     """
#     List all snippets, or create a new snippet.
#     """
#     authentication_classes = (authentication.TokenAuthentication,)
#     permission_classes = []
#
#     @detail_route(methods=['get'], url_path='me')
#     def me(self, request, format=None):
#         user = User.objects.get(id=request.user.id)
#         serializer = UserSerializer(user, many=False)
#         return Response(serializer.data)



#
#
# class ProfileViewSet(viewsets.ModelViewSet):
#     @detail_route()
#     def info(self, request, *args, **kwargs):
#         # assumes the user is authenticated, handle this according your needs
#         user_id = request.user.id
#         return self.retrieve(request, user_id)
#
from rest_framework.urlpatterns import format_suffix_patterns




@api_view(['GET'])
@protected_resource(scopes=['read'])
def me_view(request, format=None):
    user_id = request.user.id
    print request.user
    return Response(UserSerializer(request.user).data)
    # return self.retrieve(request, user_id)
    pass

# Routers provide an easy way of automatically determining the URL conf
router_v1 = routers.DefaultRouter()
router_v1.register(r'/me', me_view, base_name="me")
# router_v1.register(r'groups', GroupViewSet)
apipatterns = [
     url(r'^me/$', me_view),
]
#
urlpatterns = format_suffix_patterns(apipatterns, allowed=['json', 'html', 'api'])

# urlpatterns = router_v1.urls
