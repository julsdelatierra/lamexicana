#encoding:utf-8
from django.shortcuts import render_to_response as render
from django.template.context import RequestContext as rc
from forms import SignForm

def new(request):
    sign_form = SignForm()
    if request.POST:
        sign_form = SignForm(request.POST)
        if sign_form.is_valid():
            sign_form.save()
            args = {}
            return render('done.html', args, context_instance=rc(request))
    args = {'sign_form':sign_form}
    return render('new.html', args, context_instance=rc(request))
