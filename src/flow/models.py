from django.db import models
from multiselectfield import MultiSelectField


class Applicant(models.Model):
    id = models.AutoField(primary_key=True)
    insurance_number = models.CharField(max_length=20, default="")
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    street_number = models.CharField(max_length=100)
    zip_code = models.IntegerField()
    city = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Applicant data for ID {self.id} (insurance number: {self.insurance_number})"


class Application(models.Model):
    id = models.AutoField(primary_key=True)
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    first_application = models.BooleanField()
    SERVICE_OPTIONS = (
        ("cash", "Geldleistung (Pflege durch eine Privatperson)"),
        ("service", "Sachleistung (Pflege durch einen Pflegedienst)"),
        ("combined", "Kombi-Leistung (Pflege durch Privatperson & Pflegedienst)"),
        ("partial inpatient", "Tages- oder Nachtpflege (teilstationär)"),
        ("inpatient", "dauerhafte Pflege im Pflegeheim"),
        (
            "inpatient with disability",
            "dauerhafte Pflege in einer Einrichtung für behinderte Menschen",
        ),
        ("medical aids", "Hilfsmittel"),
        ("unknown", "Das weiß ich nicht"),
    )
    selected_services = MultiSelectField(choices=SERVICE_OPTIONS, max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Applicant data for ID {self.id} (applicant ID: {self.applicant})"


class Consent(models.Model):
    id = models.AutoField(primary_key=True)
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    data_share = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Consent data for ID {self.id} (applicant ID: {self.applicant})"
