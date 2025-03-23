from django.urls import path
from .views_api import (
    AdminSignupView, AdminLoginView, BookCreateView, BookListView, BookDetailView
)
from .views_panel import (
    admin_login, admin_logout, admin_dashboard, admin_create_book,
    admin_update_book, admin_delete_book, student_book_list
)

urlpatterns = [
    # API endpoints (prefixed with 'api/')
    path('api/admin/signup/', AdminSignupView.as_view(), name='api-admin-signup'),
    path('api/admin/login/', AdminLoginView.as_view(), name='api-admin-login'),
    path('api/books/', BookListView.as_view(), name='api-book-list'),
    path('api/books/create/', BookCreateView.as_view(), name='api-book-create'),
    path('api/books/<int:pk>/', BookDetailView.as_view(), name='api-book-detail'),

    # Admin Panel views (direct URLs)
    path('admin-panel/login/', admin_login, name='admin-login'),
    path('admin-panel/logout/', admin_logout, name='admin-logout'),
    path('admin-panel/dashboard/', admin_dashboard, name='admin-dashboard'),
    path('admin-panel/books/create/', admin_create_book, name='admin-create-book'),
    path('admin-panel/books/<int:pk>/update/', admin_update_book, name='admin-update-book'),
    path('admin-panel/books/<int:pk>/delete/', admin_delete_book, name='admin-delete-book'),

    # Student view (direct URL)
    path('student/books/', student_book_list, name='student-book-list'),
]
