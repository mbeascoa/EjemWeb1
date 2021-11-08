from django.http import HttpResponse



def index(request):
    return HttpResponse("<h1>Miguel Angel</h1><h2>Beascoa<h2><h2>Alzola<h2>")