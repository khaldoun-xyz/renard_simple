from django import forms

from .models import Applicant


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
