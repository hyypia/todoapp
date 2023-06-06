from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def todo_view(request):
    if request.method == "POST":
        return HttpResponse(request.POST["title"], status=201)
