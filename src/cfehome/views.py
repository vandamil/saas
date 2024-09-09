from django.http import HttpResponse
from django.shortcuts import render
from visits.models import PageVisit
import pathlib

this_dir = pathlib.Path(__file__).resolve().parent

def home_page_view(request,*args,**kwargs):
    my_title = "My Page - (in views.py)"
    my_context = {
        "page_title":my_title,
        "page_visit_count":PageVisit.objects.filter(path=request.path).count(),
        "total_visit_count":PageVisit.objects.all().count(),
    }

    PageVisit.objects.create(path = request.path)
    ht_temp = "home.html"

    
    
    return render(request,ht_temp,my_context) 

def old_home_page_view(request,*args,**kwargs):
    ht = ""
    ht_fp = this_dir/"home.html"
    ht = ht_fp.read_text()
    
    
    return HttpResponse(ht)