from django.urls import path
from . import views

app_name = 'book_app'

urlpatterns = [
    path('', views.index, name='home'),
    path('<id>', views.Single_Book, name='review'),
]
