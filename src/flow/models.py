from django.db import models


class Applicant(models.Model):
    id = models.AutoField(primary_key=True)
    insurance_number = models.CharField(max_length=20, default="")
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    street_number = models.CharField(max_length=100)
    zip_code = models.IntegerField()
    city = models.CharField(max_length=50)

    def __str__(self):
        return f"Applicant data for ID {self.id} (insurance number: {self.insurance_number})"


class Consent(models.Model):
    id = models.AutoField(primary_key=True)
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    data_share = models.BooleanField()

    def __str__(self):
        return f"Consent data for ID {self.id} (applicant ID: {self.applicant})"
