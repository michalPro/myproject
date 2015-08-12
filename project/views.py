from django.shortcuts import render
from django.http import Http404, HttpResponse
import datetime


def hello(request):
    return HttpResponse("Hello world")


def get_example(request):
    example = [20, 30, 40]
    return render(request, 'example/example.html', {'example': example})


def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'datetime/current_datetime.html', {'current_date': now})


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)
