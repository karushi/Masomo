from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,Http404
from .models import Grade,Student,Subject



# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):
    students = Student.objects.all()
    return render(request,'index.html',{"students":students})


@login_required(login_url="/accounts/login/")
def search_results(request):
    if 'Name' in request.GET and request.GET["Name"]:
        search_term = request.GET.get("Name")
        searched_name = Student.search_by_name("search_term")
        message = f"{search_term}"

        return render(request,'search.html',{"message":message,"name":searched_name})
    else:
        message = "You haven't searched for any term"
        return render(request,'search.html',{"message":message})
