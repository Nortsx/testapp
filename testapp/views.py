from django.http import HttpResponse


def index(request):
    return HttpResponse("You're looking at index htmlss")