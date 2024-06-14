from django.shortcuts import render, HttpResponse

from library.models import Book

# Create your views here.
'''
创建一个项目，用来说明出版社，书籍和作者的关系。
假定关系：作番：书籍 =>1:n（一本书由一个作者完成，一个作者可以创作多本书）
出版社：书籍 >n:n（一个出版社可以出版多本书，一本书可以由多个出版社出版）
要求：
1. 在书籍的book_index.htm1中有一个"查看所有书籍”的超链接按钮，点击进入书籍列表book_1ist.html页面.
2.在书籍的book_1ist.htm1中显示所有书名，点击书名可以进入书籍详情book_detail.htm1（通过书籍id）
3.在书籍book_detail.htm1中可以点击该书的作者和出版社，
进入作者详情的author_detai1.htm1和出版社详情的publisher_detai1.html页面
'''

from .models import Author, Publisher, Book
import random


def add_book(request):
    # Sample data
    author_names = [
        'J.K. Rowling', 'George R.R. Martin', 'J.R.R. Tolkien', 'Agatha Christie', 'Stephen King',
        'Isaac Asimov', 'Arthur C. Clarke', 'Douglas Adams', 'Jane Austen', 'Mark Twain',
        'Charles Dickens', 'Ernest Hemingway', 'F. Scott Fitzgerald', 'Leo Tolstoy', 'H.G. Wells',
        'Mary Shelley', 'Bram Stoker', 'Oscar Wilde', 'H.P. Lovecraft', 'J.D. Salinger'
    ]

    publisher_names = [
        'Penguin Books', 'HarperCollins', 'Simon & Schuster', 'Hachette Livre', 'Macmillan Publishers',
        'Random House', 'Scholastic', 'Houghton Mifflin Harcourt', 'Oxford University Press',
        'Cambridge University Press'
    ]

    book_titles = [
        'Harry Potter and the Sorcerer\'s Stone', 'A Game of Thrones', 'The Fellowship of the Ring',
        'Murder on the Orient Express', 'The Shining', 'Foundation', '2001: A Space Odyssey',
        'The Hitchhiker\'s Guide to the Galaxy', 'Pride and Prejudice', 'Adventures of Huckleberry Finn',
        'A Tale of Two Cities', 'The Old Man and the Sea', 'The Great Gatsby', 'War and Peace', 'The Time Machine',
        'Frankenstein', 'Dracula', 'The Picture of Dorian Gray', 'The Call of Cthulhu', 'The Catcher in the Rye'
    ]

    # Create Authors
    authors = []
    for name in author_names:
        authors.append(Author(name=name))
    Author.objects.bulk_create(authors)

    # Create Publishers
    publishers = []
    for name in publisher_names:
        publishers.append(Publisher(name=name))
    Publisher.objects.bulk_create(publishers)

    # Create Books
    authors = list(Author.objects.all())
    publishers = list(Publisher.objects.all())
    books = []
    for title in book_titles:
        author = random.choice(authors)
        book = Book(title=title, author=author)
        book.save()
        book.publisher.set(random.sample(publishers, k=random.randint(1, 3)))
        books.append(book)

    return HttpResponse("Sample data has been added successfully!")

def index(request):
    return render(request, 'index.html')

def get_all_books(request):
    books = Book.objects.all()
    return render(request, 'books.html', {'books': books})

def get_book_detail(request, book_title):
    book_info = Book.objects.get(title=book_title)
    return render(request, 'book_detail.html', {'book': book_info})
def get_book_author(request, author_name):
    author_info = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author_name)
    return render(request, 'author_detail.html', {'author': author_info, 'books': books})

def get_book_publisher(request):
    pass
