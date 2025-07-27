from django import forms

from .models import Genre


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ["id", "name", "description", "active"]
