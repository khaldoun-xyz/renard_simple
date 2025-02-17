from django import forms

from .models import Applicant, Application, Consent


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
        labels = {
            "insurance_number": "Versicherungsnummer",
            "first_name": "Vorname",
            "last_name": "Nachname",
            "street_number": "Strasse und Hausnummer",
            "zip_code": "Postleitzahl",
            "city": "Stadt",
        }


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = (
            "first_application",
            "selected_services",
        )
        labels = {
            "first_application": "Erstantrag",
            "selected_services": "Leistungen, für die der Antrag gestellt wird",
        }


class ConsentForm(forms.ModelForm):
    class Meta:
        model = Consent
        fields = ("data_share",)
        labels = {
            "data_share": "Hiermit erteile ich die nachfolgend verlinkte Schweigepflichtentbindung und Einwilligungserklärung."
        }
