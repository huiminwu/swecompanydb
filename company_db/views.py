from django.shortcuts import render,HttpResponse

from . import utils
from .models import Company, CompanyRep


def export_csv(request):
  # Create the HttpResponse object with the appropriate CSV header.
  data = utils.download_csv(request, CompanyRep.objects.order_by('company'))
  response = HttpResponse(data, content_type="text/csv")
  return response


def home(request):
    return render(request, "home.html", {"title": "home"})

def about(request):
    return render(request, "templates/company_db/about.html", {"title": "about"})
