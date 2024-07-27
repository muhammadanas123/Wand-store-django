from django import forms
from .models import WandVariety


class WandVarietyForm(forms.Form):
  wand_variety = forms.ModelChoiceField(queryset=WandVariety.objects.all(), label='select the wand variety')
