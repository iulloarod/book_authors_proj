from django.urls import path
from . import views

urlpatterns = [
    path('', views.books),
    path('authors', views.authors),
    path('authors/<int:id>', views.authorsid),
    path('books/<int:id>', views.booksid),
]
