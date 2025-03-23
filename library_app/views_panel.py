from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import AdminLoginForm, BookForm
from .models import Book

# Admin Panel Login View
def admin_login(request):
    if request.method == 'POST':
        form = AdminLoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            login(request, user)  # Create session
            return redirect('admin-dashboard')
    else:
        form = AdminLoginForm()
    return render(request, 'library_app/admin/login.html', {'form': form})

# Admin Panel Logout View
def admin_logout(request):
    logout(request)
    return redirect('admin-login')

# Admin Dashboard: List Books
@login_required(login_url='admin-login')
def admin_dashboard(request):
    books = Book.objects.all()
    return render(request, 'library_app/admin/dashboard.html', {'books': books})

# Create Book (Admin Panel)
@login_required(login_url='admin-login')
def admin_create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin-dashboard')
    else:
        form = BookForm()
    return render(request, 'library_app/admin/create_book.html', {'form': form})

# Update Book (Admin Panel)
@login_required(login_url='admin-login')
def admin_update_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('admin-dashboard')
    else:
        form = BookForm(instance=book)
    return render(request, 'library_app/admin/update_book.html', {'form': form, 'book': book})

# Delete Book (Admin Panel)
@login_required(login_url='admin-login')
def admin_delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('admin-dashboard')
    return render(request, 'library_app/admin/delete_book.html', {'book': book})

# Student View: List Books
def student_book_list(request):
    books = Book.objects.all()
    return render(request, 'library_app/student/book_list.html', {'books': books})
