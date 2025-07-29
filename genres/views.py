# from django.views.generic import ListView

import json

from django.http import JsonResponse
from django.shortcuts import get_list_or_404, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from .models import Genre


@csrf_exempt
def GenreListView(request):
    if request.method == "GET":
        genres = get_list_or_404(Genre, active=True)
        data = [
            {
                "id": gr.id,
                "name": gr.name,
                "description": gr.description,
                "active": gr.active,
            }
            for gr in genres
        ]
        return JsonResponse({"genres": data})
    elif request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        new_genre = Genre(
            name=data.get("name"),
            description=data.get("description"),
            active=data.get("active"),
        )
        new_genre.save()
        data = {"id": new_genre.id, "name": new_genre.name}
        return JsonResponse(data, status=201)


@csrf_exempt
def GenreDetailView(request, pk):
    if request.method == "GET":
        genre_detail = get_object_or_404(Genre, pk=pk)
        data = {
            "id": genre_detail.id,
            "name": genre_detail.name,
            "description": genre_detail.description,
            "active": genre_detail.active,
        }
        return JsonResponse(data)
