from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import ApplicantForm, ApplicationForm, ConsentForm
from .models import Applicant, Application


def index(request: HttpRequest) -> HttpResponse:
    return render(request, template_name="flow/index.html")


def add_applicant(request: HttpRequest) -> HttpResponse:
    form = ApplicantForm(data=request.POST or None)
    if form.is_valid():
        new_applicant = form.save()
        redirect_url = reverse("flow:add_application", args=[new_applicant.id])
        return redirect(to=redirect_url)
    return render(request, "flow/add_applicant_form.html", {"form": form})


def edit_applicant(request: HttpRequest, applicant_id: int):
    applicant = Applicant.objects.get(pk=applicant_id)
    form = ApplicantForm(request.POST or None, instance=applicant)
    if form.is_valid():
        form.save()
        redirect_url = reverse("flow:review", args=[applicant_id])
        return redirect(to=redirect_url)
    return render(
        request,
        "flow/edit_applicant_form.html",
        {"form": form, "applicant_id": applicant_id},
    )


def add_application(request: HttpRequest, applicant_id: int) -> HttpResponse:
    applicant_data = Applicant.objects.get(pk=applicant_id)
    form = ApplicationForm(data=request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.applicant = applicant_data
        obj.save()
        redirect_url = reverse("flow:review", args=[applicant_id])
        return redirect(to=redirect_url)
    return render(request, "flow/add_application_form.html", {"form": form})


def edit_application(request: HttpRequest, applicant_id: int):
    application = (
        Application.objects.filter(applicant_id=applicant_id)
        .order_by("-created_at")
        .first()
    )
    form = ApplicationForm(request.POST or None, instance=application)
    if form.is_valid():
        form.save()
        redirect_url = reverse("flow:review", args=[applicant_id])
        return redirect(to=redirect_url)
    return render(
        request,
        "flow/edit_application_form.html",
        {"form": form, "applicant_id": applicant_id},
    )


def review(request: HttpRequest, applicant_id: int) -> HttpResponse:
    applicant = Applicant.objects.get(pk=applicant_id)
    application = (
        Application.objects.filter(applicant_id=applicant_id)
        .order_by("-created_at")
        .first()
    )
    form = ConsentForm(data=request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.applicant = applicant
        obj.save()
        return redirect(to="flow:confirmation")
    return render(
        request,
        "flow/review.html",
        {"form": form, "applicant": applicant, "application": application},
    )


def confirmation(request: HttpRequest) -> HttpResponse:
    return render(request, template_name="flow/confirmation.html")
