from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def todo_item(request):
    if request.method == "GET":
        return HttpResponse(status=200)
    if request.method == "POST":
        return HttpResponse(request.POST["title"], status=201)


@csrf_exempt
def todo_list(request):
    pass
