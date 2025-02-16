from django.urls import path

from . import views

app_name = "flow"

urlpatterns = [
    path("flow/", views.index, name="index"),
    path("add_applicant/", views.add_applicant, name="add_applicant"),
    path("confirmation/", views.confirmation, name="confirmation"),
]
