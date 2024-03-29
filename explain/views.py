from django.shortcuts import render

from django.http import HttpResponse


def explainindex(request):
    template_name = 'explain/explainindex.html'
    return render(request, template_name)

