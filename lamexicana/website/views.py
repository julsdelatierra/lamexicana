#encoding:utf-8
from django.shortcuts import render_to_response as render
from django.template.context import RequestContext as rc
from django.http import HttpResponse as response
from models import Article

# Create your views here.
def error404(request):
    return response('404')

def error500(request):
    return response('500')

def index(request):
    args = {'articles':Article.objects.all().order_by('date_creation')[:3]}
    return render('index.html', args, context_instance=rc(request))
