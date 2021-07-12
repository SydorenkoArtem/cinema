from django.db import models
from django.utils.text import slugify


class Genre(models.Model):
    """Genre model implementation"""

    genre = models.CharField(unique=True, max_length=255)

    class Meta:
        verbose_name = "genre"
        verbose_name_plural = "genres"
        ordering = ["genre"]

    def __repr__(self):
        """Return a string representation of a model"""

        return f"<Genre ({self.pk}) {self}>"

    def __str__(self):
        """Return a string version of an instance"""

        return self.genre


class Film(models.Model):
    """Film model implementation"""

    film = models.CharField(unique=True, max_length=255)
    description = models.TextField()
    slug = models.SlugField(max_length=255, blank=True, unique=True)
    pic = models.ImageField(upload_to="static/images/film")
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT)

    class Meta:
        db_table = "film"
        ordering = ["genre"]

    def __repr__(self):
        """Return a string representation of an instance"""

        return f"<Film ({self.pk}) '{self}'>"

    def __str__(self):
        """Return a string version of an instance"""

        return self.film

    def save(self, *args, **kwargs):
        """Save object with slugify"""

        if not self.slug:
            self.slug = slugify(self.film)

        super(Film, self).save(*args, **kwargs)
