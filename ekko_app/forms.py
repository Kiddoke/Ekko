from django import forms
from ekko_app.models import Ansatt

class SMSForm(forms.Form):
    recipients = forms.ModelMultipleChoiceField(
        queryset=Ansatt.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            "oninput": "updateCharCounter()",
            "maxlength": "610",
            "class": "border rounded p-2 w-full"
        }),
    )

    def clean_message(self):
        message = self.cleaned_data.get("message")
        normalized = message.replace("\r\n", "\n")
        print("Lengde etter normalisering:", len(normalized))

        if len(normalized) > 610:
            raise forms.ValidationError("Meldingen er for lang (maks 610 tegn).")

        return normalized