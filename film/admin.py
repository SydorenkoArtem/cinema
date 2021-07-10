from django.contrib import admin

from film.models import Genre, Film


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Genre admin implementation"""

    fields = [
        "genre",
    ]


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    """Film admin implementation"""

    fields = [
        "genre",
        "pic",
        "slug",
        "film",
        "description",
    ]

    prepopulated_fields = {"slug": ["film"]}

    list_display = [
        "film",
        "genre",
    ]

    list_display_links = [
        "film",
    ]

    list_filter = ["genre"]
