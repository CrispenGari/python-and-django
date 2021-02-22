from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def main(req):
    template = loader.get_template('basic/index.html')
    context = {'name': "This is my name!!"}
    return HttpResponse(template.render(context, req))
