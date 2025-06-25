from django.contrib.auth import get_user_model
from home.serializers import UserSerializer
from novadata_utils.viewsets import NovadataModelViewSet


class UserViewSet(NovadataModelViewSet):
    User = get_user_model()
    queryset = User.objects.all()

    serializer_class = UserSerializer

    search_fields = []
