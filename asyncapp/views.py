from operator import le
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django_celery_results.models import TaskResult
from django.template import loader
from .tasks import insert


def asyncapp(requests):
    template = loader.get_template("async.html")
    if "exe_button" in requests.POST:
        insert.delay(requests.POST["word"])

    task_results = TaskResult.objects.all().values_list(
        "result", "task_id", "status", "date_done"
    )

    context = {"task_results": task_results}

    if requests.method == "POST":
        return HttpResponseRedirect("/asyncapp")
    else:
        return render(requests, "async.html", context)
