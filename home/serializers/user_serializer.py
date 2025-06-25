from django.contrib.auth import get_user_model
from novadata_utils.serializers import NovadataModelSerializer


class UserSerializer(NovadataModelSerializer):
    class Meta:
        User = get_user_model()
        model = User
        fields = "__all__"
