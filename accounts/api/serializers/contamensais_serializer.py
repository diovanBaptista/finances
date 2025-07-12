from rest_framework import serializers

from ...models import ContaMensais


class ContaMensaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContaMensais
        fields = '__all__'
