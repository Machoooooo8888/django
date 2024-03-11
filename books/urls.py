from django.urls import path
from .views import *


urlpatterns = [
    path('book/',book_get),
    path('book-create/', book_create ),
    path('book/<int:pk>/', book_id)
]