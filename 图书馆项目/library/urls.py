from django.urls import path
from library.views import *

urlpatterns = [
    path('index/', index, name='index' ),
    path('addbook', add_book, name='addbook'),
    path('allbooks/', get_all_books, name='allbooks'),
    path('book/<str:book_title>/', get_book_detail, name='book_detail'),
    path('author_detail/<str:author_name>', get_book_author, name='author_detail'),
    path('publisher_detail/<str:publisher_name>/', get_book_publisher, name='publisher_detail')
]