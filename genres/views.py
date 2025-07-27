from django.views.generic import ListView

from .models import Genre


class GenreListView(ListView):
    model = Genre
    context_object_name = "genres"
    ordering = ["name"]

    def get_queryset(self):
        return Genre.objects.filter(active=True)
