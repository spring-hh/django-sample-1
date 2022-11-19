from django.shortcuts import render
import json

# Create your views here.
def drapdrop2(request):
    if request.method == "POST":
        # get post body
        body = request.body
        # decode body json
        body_unicode = body.decode('utf-8')
        body_json = json.loads(body_unicode)

        for item in body_json:
            print(item.get('id'))
            print(item.get('name'))
            print(item.get('target'))
            print(item.get('editFlg'))

    return render(request, "dragdrop2.html")
