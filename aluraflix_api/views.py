from django.http import JsonResponse

# Create your views here.

def todos_videos(request):
    if request.method == 'GET':
        videos = {'id':'All', 'titulo':'All_title','dercição':'All','url':'All-urls'}
        return JsonResponse(videos)