from django.shortcuts import render

from django.http import HttpResponse


def homeindex(request):
    template_name = 'homepage/homeindex.html'
    return render(request, template_name)
