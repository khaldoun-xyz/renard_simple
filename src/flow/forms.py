from django import forms

from .models import Applicant, Application, Consent


class ApplicantForm(forms.ModelForm):
    birth_date = forms.DateField(
        input_formats=["%d.%m.%Y"],  # Add custom date format (DD.MM.YYYY)
        widget=forms.DateInput(
            format="%d.%m.%Y"
        ),  # Optionally specify the input widget format
    )

    class Meta:
        model = Applicant
        fields = (
            "insurance_number",
            "first_name",
            "last_name",
            "birth_date",
            "street_number",
            "zip_code",
            "city",
            "phonenumber",
            "email",
        )
        labels = {
            "insurance_number": "Versicherungsnummer",
            "first_name": "Vorname",
            "last_name": "Nachname",
            "birth_date": "Geburtsdatum",
            "street_number": "Strasse und Hausnummer",
            "zip_code": "Postleitzahl",
            "city": "Stadt",
            "phonenumber": "Telefonnummer",
            "email": "E-Mail-Adresse",
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
    data_share = forms.BooleanField(
        required=True,
        label="Hiermit erteile ich die nachfolgend verlinkte Schweigepflichtentbindung und Einwilligungserklärung.",
    )

    class Meta:
        model = Consent
        fields = ("data_share",)
        labels = {
            "data_share": "Hiermit erteile ich die nachfolgend verlinkte Schweigepflichtentbindung und Einwilligungserklärung."
        }
