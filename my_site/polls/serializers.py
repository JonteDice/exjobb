from rest_framework import serializers
from .models import Poll

class CreatePollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = ['question', 'answer_1', 'answer_2', 'answer_3']