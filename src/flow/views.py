from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import ApplicantForm, ConsentForm
from .models import Applicant


def index(request: HttpRequest) -> HttpResponse:
    return render(request, template_name="flow/index.html")


def add_applicant(request: HttpRequest) -> HttpResponse:
    form = ApplicantForm(data=request.POST or None)
    if form.is_valid():
        new_applicant = form.save()
        redirect_url = reverse("flow:review", args=[new_applicant.id])
        return redirect(to=redirect_url)
    return render(request, "flow/add_applicant_form.html", {"form": form})


def review(request: HttpRequest, applicant_id) -> HttpResponse:
    applicant_data = Applicant.objects.get(pk=applicant_id)
    form = ConsentForm(data=request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.applicant = applicant_data
        obj.save()
        return redirect(to="flow:confirmation")
    return render(
        request, "flow/review.html", {"form": form, "applicant_data": applicant_data}
    )


def confirmation(request: HttpRequest) -> HttpResponse:
    return render(request, template_name="flow/confirmation.html")
