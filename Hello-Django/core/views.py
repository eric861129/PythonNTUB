import datetime

from django.http.response import HttpResponse

def hello(request):
    print(request.GET)
    if request.GET and "name" in request.GET:
        return HttpResponse(str(request.GET["name"]))
    return HttpResponse('<h1>Hello World</h1>')

