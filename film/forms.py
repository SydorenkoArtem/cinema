from django import forms

from film.models import Film


class FilmUpdateForm(forms.ModelForm):
    """Film Update form implementation"""

    class Meta:
        model = Film
        fields = '__all__'


class FilmDeleteForm(forms.ModelForm):
    """Film Delete form implementation"""

    class Meta:
        model = Film
        fields = '__all__'
