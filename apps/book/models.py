from django.db import models


# Create your models here.
class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=False, null=False)
    last_name = models.CharField(max_length=200, blank=False, null=False)
    nationality = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    state = models.BooleanField("State", default=True)
    creation_date = models.DateField('Creation Date', auto_now=True, auto_now_add=False)

    # It's works for the name in the admin page
    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
        ordering = ['name']

    # In the list of Authors this class return the name of the model
    def __str__(self):
        return self.name


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('Tittle', max_length=255, blank=False, null=False)
    publication_date = models.DateField('Publication Date', blank=False, null=False)
    author_id = models.ManyToManyField(Author)
    creation_date = models.DateField('Creation Date', auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        ordering = ['title']

    def __str__(self):
        return self.title
