# from django.views.generic import ListView

import json

from django.http import JsonResponse

from .models import Genre

# class GenreListView(ListView):
#     model = Genre
#     context_object_name = "genres"
#     ordering = ["name"]

#     def get_queryset(self):
#         return Genre.objects.filter(active=True)


def GenreListView(request):
    if request.method == "GET":
        genres = Genre.objects.filter(active=True).values(
            "id", "name", "description", "active"
        )
        data = list(genres)
        return JsonResponse({"genres": data})
    elif request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
