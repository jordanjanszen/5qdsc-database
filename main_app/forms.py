from django.forms import ModelForm
from .models import Trial

class TrialForm(ModelForm):
  class Meta:
    model = Trial
    fields = ['date', 'name', 'judge', 'score']