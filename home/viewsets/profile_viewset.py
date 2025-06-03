from home.models import Profile
from home.serializers import ProfileSerializer
from novadata_utils.viewsets import NovadataModelViewSet


class ProfileViewSet(NovadataModelViewSet):
    queryset = Profile.objects.all()

    serializer_class = ProfileSerializer
    permission_classes = []

    search_fields = []
