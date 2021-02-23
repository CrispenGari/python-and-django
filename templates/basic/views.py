from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def main(req):
    template = loader.get_template('basic/index.html')
    context = {
    }
    return HttpResponse(template.render(context, req))

def history(req, hist_id):
    template = loader.get_template('basic/history.html')
    context ={
        'id': hist_id,
    }
    return HttpResponse(template.render(context, req))

def about(req):
    template = loader.get_template('basic/about.html')
    context ={}
    return HttpResponse(template.render(context, req))