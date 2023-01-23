from django.urls import path,include
from books_api.views import book_list

urlpatterns = [
    path('lists/',book_list),
]
