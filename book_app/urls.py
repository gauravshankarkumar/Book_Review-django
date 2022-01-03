from django.urls import path
from . import views

app_name = 'book_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('book/<id>', views.review, name='review'),
    path('add_review/<id>', views.add_review, name='add_review'),
]
