from django.shortcuts import render
from firstlesson.models import Restaurant

def home_view(request):
    myrestaurant = Restaurant.objects.first()
    context = {
        "zeytun": 55,
        "restaurant": myrestaurant,
    }
    return render(request, "index.html", context)




