from django.shortcuts import render, HttpResponse, redirect
from .models import Book, Author

#template que permite añadir un libro y a la vez muestra la lista de libros existentes en la DB
def books(request):
    book_tables = Book.objects.all()
    if request.method == "GET":
        context= {
            "book_tables": book_tables,
        }
        return render(request,"books.html", context)
    if request.method=="POST":
        new_title = request.POST['new_title']
        new_desc = request.POST['new_desc']
        print(f'added Title {new_title} and description: {new_desc}')
        Book.objects.create(title=new_title, desc=new_desc)
        return redirect("/")
        

#template que permite añadir un autor y a la vez muestra muestra los autores existentes en la DB
def authors(request):
    author_tables = Author.objects.all()
    if request.method == "GET":
        context= {
            "author_tables": author_tables,
        }
        return render(request,"authors.html", context)
    if request.method=="POST":
        new_autor_f_name = request.POST['new_f_name']
        new_autor_l_name = request.POST['new_l_name']
        new_autor_notes = request.POST['new_notes']
        print(f'added Author {new_autor_f_name} {new_autor_l_name} and Notes: {new_autor_notes}')
        Author.objects.create(first_name=new_autor_f_name, last_name=new_autor_l_name, notas= new_autor_notes)
        return redirect("/authors")


#template que muestra un libro existentes en la DB y permite asignar más autores a la db.
def booksid(request, id):
    book_info = Book.objects.get(id=int(id))
    author_info = Author.objects.get(id=int(id))
    author_list = Author.objects.all()
    book_author= book_info.authors.all()
    context= {
            "book_id": book_info.id,
            "book_title": book_info.title,
            "book_desc": book_info.desc,
            "book_author": book_author,
            "author_list": author_list,
        }
    if request.method == "GET":
        return render(request,"booksid.html", context)
    if request.method == "POST":
        new_author = request.POST['new_author_option']
        add_author = Author.objects.filter(first_name__contains = new_author)
        print(add_author)
        return render(request,"booksid.html", context)

#template que muestra un autor existente en la DB y permite asignar más libros a la db.
def authorsid(request, id):
    author_info = Author.objects.get(id=int(id))
    book_info = Book.objects.all()
    context= {
            "id": author_info.id,
            "first_name": author_info.first_name,
            "last_name": author_info.last_name,
            "books": author_info.books.all(),
            "notes": author_info.notas,
            "book_list": book_info,
        }
    if request.method == "GET":
        return render(request,"authorsid.html", context)
    if request.method == "POST":
        new_b_title = request.POST['new_title_option']
        book = Book.objects.filter(title=new_b_title)
        book_id = book[0].id
        author_info.books.add(book_id)
        return render(request,"authorsid.html", context)