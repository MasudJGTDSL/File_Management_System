from django.http import HttpResponse

def index(request):
    return HttpResponse("Home page created for first time............!")

