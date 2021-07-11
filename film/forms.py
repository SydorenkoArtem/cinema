from django import forms

from film.models import Film


class FilmUpdateForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = '__all__'


class FilmDeleteForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = '__all__'
