from django.urls import path

from shelves import views
from shelves import models

urlpatterns = [
    path('', views.index_view, name='index'),
]

authors = models.Author.objects.all()
for author in authors:
    urlpatterns += [
        path(
            f'authors/{author.id}/',
            views.author_view,
            kwargs={'author_id': author.id},
            name=f'author_{author.id}'
        )
    ]
