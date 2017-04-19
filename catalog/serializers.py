# TODO use API or remove it
from rest_framework import serializers
# from .models import Institution, LANGUAGE_CHOICES, STYLE_CHOICES
from .models import Institution

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields = ('id', 'name', 'city')