from django.http import HttpResponse,JsonResponse
def home_page(request):
    print("home page requested")
    Friends = [
        'Ankit',
        'Alankrit',
        'Shai'
    ]
    return JsonResponse(Friends,safe=False)