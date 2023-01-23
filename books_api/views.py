from django.shortcuts import render
from models import *
from django.http import JsonResponse

# Create your views here.
def book_list(request):
    books = Book.objects.all()
    booksPython = list(books.values())  #convert into python ds
    return  JsonResponse({
        'books': booksPython
    })




