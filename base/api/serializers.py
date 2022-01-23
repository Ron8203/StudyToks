# Since python objects can't be sent directly (eg Room). SO to send these we first need to convert them into json objects to do this we use serializers

from rest_framework.serializers import ModelSerializer
from base.models import Room

class RoomSerializer(ModelSerializer):
      class Meta:
          model = Room
          fields = '__all__'