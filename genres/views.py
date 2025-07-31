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
            active=data.get("active", True),
        )
        new_genre.save()
        data = {"id": new_genre.id, "name": new_genre.name}
        return JsonResponse(data, status=201)


@csrf_exempt
def GenreDetailView(request, pk):
    genre = get_object_or_404(Genre, pk=pk)

    if request.method == "GET":
        data = {
            "id": genre.id,
            "name": genre.name,
            "description": genre.description,
            "active": genre.active,
        }
        return JsonResponse(data)

    elif request.method == "PUT":
        data = json.loads(request.body.decode("utf-8"))
        genre.name = data.get("name", genre.name)
        genre.description = data.get("description", genre.description)
        genre.active = data.get("active", genre.active)
        genre.save()
        data = {
            "id": genre.id,
            "name": genre.name,
            "description": genre.description,
            "active": genre.active,
        }
        return JsonResponse(data, status=200)

    elif request.method == "DELETE":
        genre.delete()
        return JsonResponse(
            {"message": "Genre deleted successfully."}, status=204
        )
