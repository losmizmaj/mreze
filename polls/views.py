from django.http import HttpResponse


def index(request):
    return HttpResponse("Volem sarmu vise no slaninu")
