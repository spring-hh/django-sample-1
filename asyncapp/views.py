from django.shortcuts import render
from django.http import HttpResponseRedirect
from django_celery_results.models import TaskResult
from .tasks import insert
from .models import Result
from django.db.models import Q


def asyncapp(requests):
    if requests.method == "POST":
        if "exe_button" in requests.POST:
            insert.delay(requests.POST["word"])

        return HttpResponseRedirect("/asyncapp")
    else:
        task_results = TaskResult.objects.all().values_list(
            "result", "task_id", "status", "date_done"
        )

        results = Result.objects.filter(
            ~Q(task_id__in=[task[1] for task in task_results])
        )

        # structured programming: loop over task_results and results
        # and compare task_id of each item in both lists and update
        # status and date_done of each item in results list
        for task in task_results:
            for result in results:
                if task[1] == result.task_id:
                    result.status = task[2]
                    result.date_done = task[3]
                    result.save()

        context = {"task_results": task_results, "results": results}
        return render(requests, "async.html", context)
