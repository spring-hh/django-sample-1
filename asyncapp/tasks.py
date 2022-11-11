from __future__ import absolute_import, unicode_literals
import datetime
import time
from celery import shared_task

from asyncapp.models import Result


@shared_task
def insert(word):
    # get task id
    task_id = insert.request.id
    print(task_id)

    # insert into database
    Result.objects.create(
        task_id=task_id,
        result=word,
        status="PENDING",
        date_start=datetime.datetime.now(),
    )

    time.sleep(20)
    return word
