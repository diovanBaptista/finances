from home.models import Profile
from rest_framework import serializers

from novadata_utils.serializers import NovadataModelSerializer


class ProfileSerializer(serializers.ModelSerializer):
    accounts_month = serializers.ReadOnlyField()
    class Meta:
        model = Profile
        fields = "__all__"
