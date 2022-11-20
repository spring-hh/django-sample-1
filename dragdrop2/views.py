from django.http import JsonResponse
from django.shortcuts import redirect, render
import json
from .models import Convert

# Create your views here.
def drapdrop2(request):
    if request.method == "POST":
        # get post body
        body = request.body
        # decode body json
        body_unicode = body.decode("utf-8")
        body_json = json.loads(body_unicode)

        for item in body_json:
            print(item.get("id"))
            print(item.get("name"))
            print(item.get("target"))
            print(item.get("editFlg"))
            Convert.objects.create(
                name=item.get("name"),
                target=item.get("target"),
            )
        
        # get data from db and conver to json
        data = Convert.objects.all().values("id", "name", "target")
        data_json = list(data)
        # return JsonResponse
        return JsonResponse(data_json, safe=False)

        
    elif request.method == "GET":
        if request.headers.get("Content-Type") == "application/json":
            data = Convert.objects.all().values("id", "name", "target")
            data_json = list(data)
            return JsonResponse(data_json, safe=False)
        else:
            # get all data
            data = Convert.objects.all()
            # set context
            context = {"data": data}
            return render(request, "dragdrop2.html", context)

