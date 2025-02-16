from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from .forms import ApplicantForm


def index(request: HttpRequest) -> HttpResponse:
    return render(request, template_name="flow/index.html")


def add_applicant(request: HttpRequest) -> HttpResponse:
    form = ApplicantForm(data=request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(to="flow:review")
    return render(request, "flow/add_applicant_form.html", {"form": form})


def review(request: HttpRequest) -> HttpResponse:
    return render(request, template_name="flow/review.html")


def confirmation(request: HttpRequest) -> HttpResponse:
    return render(request, template_name="flow/confirmation.html")
