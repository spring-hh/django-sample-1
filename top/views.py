from django.shortcuts import render

# Create your views here.


def top(requests):
    return render(requests, "top.html")
