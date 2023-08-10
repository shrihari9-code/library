import datetime
from django.shortcuts import render, redirect
from .models import Book, User
import logging  # Import the logging module

# Set up logging
logger = logging.getLogger(__name__)

def assign_book(request, user_id):
    user = User.objects.get(pk=user_id)
    
    if request.method == 'POST':
        book_id = request.POST['book']
        try:
            book = Book.objects.get(pk=book_id)
            book.is_borrowed = True
            book.borrowed_date = datetime.date.today()
            book.save()
            
            user.borrowed_book = book  # Update the user's borrowed_book field
            user.save()
            
            return redirect('user_list')  # Redirect to the appropriate page after assignment
        except Book.DoesNotExist:
            # Handle the case where the book doesn't exist
            pass
    
    available_books = Book.objects.filter(is_borrowed=False)
    return render(request, 'library/assign_book.html', {'user': user, 'available_books': available_books})

def home(request):
    books = Book.objects.all()
    return render(request, 'library/home.html', {'books': books})

def add_user(request):
    if request.method == 'POST':
        name = request.POST['name']
        contact_number = request.POST['contact_number']
        user = User(name=name, contact_number=contact_number)
        user.save()

        return redirect('user_list')

    return render(request, 'library/add_user.html')

def add_book(request):
    if request.method == 'POST':
        name = request.POST['name']
        author = request.POST['author']
        # You can add more fields here based on your Book model

        book = Book(name=name, author=author, is_borrowed=False)
        book.save()
        return redirect('home')  # Redirect to the home page or another appropriate page

    return render(request, 'library/add_book.html')  # Render the template for adding a book

def user_list(request):
    users = User.objects.all()
    return render(request, 'library/user_list.html', {'users': users})

def search_books(request):
    books = Book.objects.all()
    return render(request, 'library/search_books.html', {'books': books})