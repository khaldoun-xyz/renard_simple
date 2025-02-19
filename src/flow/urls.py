from django.urls import path

from . import views

app_name = "flow"

urlpatterns = [
    path("flow/", views.index, name="index"),
    path("add_applicant/", views.add_applicant, name="add_applicant"),
    path(
        "edit_applicant/<str:applicant_id>",
        views.edit_applicant,
        name="edit_applicant",
    ),
    path(
        "add_application/<str:applicant_id>",
        views.add_application,
        name="add_application",
    ),
    path(
        "edit_application/<str:applicant_id>",
        views.edit_application,
        name="edit_application",
    ),
    path("review/<str:applicant_id>", views.review, name="review"),
    path("confirmation/", views.confirmation, name="confirmation"),
]
