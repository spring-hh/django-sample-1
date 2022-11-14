from django.shortcuts import render

# Create your views here.
def dragdrop(requests):
    return render(requests, "dragdrop.html")
