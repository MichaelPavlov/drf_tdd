from rest_framework.serializers import ModelSerializer

from puppies.models import Puppy


class PuppySerializer(ModelSerializer):
    class Meta:
        model = Puppy
        fields = ('name', 'age', 'breed', 'color', 'created_at', 'updated_at')
