from django import forms

from .models import Applicant, Consent


class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = (
            "insurance_number",
            "first_name",
            "last_name",
            "street_number",
            "zip_code",
            "city",
        )


class ConsentForm(forms.ModelForm):
    class Meta:
        model = Consent
        fields = ("data_share",)
        labels = {
            "data_share": "Hiermit erteile ich die nachfolgend verlinkte Schweigepflichtentbindung und Einwilligungserklärung."
        }
