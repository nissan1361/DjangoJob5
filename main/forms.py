from django.forms import ModelForm

from .models import Answer, Text


class AddForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['completed', 'votes']
