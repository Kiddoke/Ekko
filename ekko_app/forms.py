from django import forms
from ekko_app.models import Ansatt

class SMSForm(forms.Form):
    recipients = forms.ModelMultipleChoiceField(
        queryset=Ansatt.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={"oninput": "updateCharCounter()", "maxlength" : "640"}),
        max_length=640
    )