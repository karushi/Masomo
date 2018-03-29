from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,Http404
from .models import Grade,Student,Subject,Fees
from django.views.generic import View
from .utils import render_to_pdf
from django.template.loader import get_template


# Create your views here.
class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        template = get_template('reportform.html')
        context = {
            'subject': 'Maths', 
            'marks': 80,
            'grade': 'A',
            'description': 'excellent',
        }
        html = template.render(context)
        pdf = render_to_pdf('reportform.html', context)
        if pdf:
             response = HttpResponse(pdf, content_type='application/pdf')
             filename = "Reportform_%s.pdf" %("12341231")
             content = "inline; filename='%s'" %(filename)
             download = request.GET.get("download")
             if download:
                 content = "attachment; filename='%s'" %(filename)
             response['Content-Disposition'] = content
             return response
        return HttpResponse("Not found")

class GeneratefeePdf(View):
    def get(self, request, *args, **kwargs):
        template = get_template('fees_structure.html')
        context = {
            'subject': 'Maths', 
            'marks': 80,
            'grade': 'A',
            'description': 'excellent',
        }
        html = template.render(context)
        pdf = render_to_pdf('fees_structure.html', context)
        if pdf:
             response = HttpResponse(pdf, content_type='application/pdf')
             filename = "Fees_structure.html_%s.pdf" %("12341231")
             content = "inline; filename='%s'" %(filename)
             download = request.GET.get("download")
             if download:
                 content = "attachment; filename='%s'" %(filename)
             response['Content-Disposition'] = content
             return response
        return HttpResponse("Not found")        
        
        


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