from django.contrib import admin

from .models import Applicant, Application, Consent

admin.site.register(Applicant)
admin.site.register(Application)
admin.site.register(Consent)
