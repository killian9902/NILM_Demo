from django.shortcuts import render

from django.http import HttpResponse


def trainingindex(request):
    template_name = 'training/trainingindex.html'
    return render(request, template_name)
