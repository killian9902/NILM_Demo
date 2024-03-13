from django.shortcuts import render

from django.http import HttpResponse


def testingindex(request):
    template_name = 'testing/testingindex.html'
    return render(request, template_name)
