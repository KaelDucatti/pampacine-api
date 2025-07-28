# from django.views.generic import ListView

from django.http import JsonResponse

from .models import Genre

# class GenreListView(ListView):
#     model = Genre
#     context_object_name = "genres"
#     ordering = ["name"]

#     def get_queryset(self):
#         return Genre.objects.filter(active=True)


def GenreListView(request):
    genres = Genre.objects.filter(active=True).values(
        "id", "name", "description", "active"
    )
    data = list(genres)
    return JsonResponse({"genres": data})
