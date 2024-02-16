from django.forms import ModelForm
from .models import Poll

class CreatePollForm(ModelForm):
    class Meta:
        model = Poll
        fields = ['question', 'answer_1', 'answer_2', 'answer_3', 'id']