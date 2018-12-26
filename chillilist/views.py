from django.http import HttpResponse
from django.http import JsonResponse
from .scraping import getScovilleVal

def chillilist(request):
    scoville =  getScovilleVal()
    return JsonResponse(scoville,safe=False)
