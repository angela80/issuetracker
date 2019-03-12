from django import forms
from .models import Issues


class IssuesForm(forms.ModelForm):

    class Meta:
        model = Issues
        fields = ('name', 'done')