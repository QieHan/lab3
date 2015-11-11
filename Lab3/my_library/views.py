# Create your views here.
#from django.shortcuts import render
#from django.http import HttpResponse
#from django import forms
#from django.contrib.auth.forms import UserCreationForm
#from django.http import HttpResponseRedirect
from django.template import Context
from django.shortcuts import render_to_response
from models import Book,Author

def first_page(request):
    return render_to_response("first_page.html")
def book_all(request):
    book_list = Book.objects.all()
    c = Context({"book_list":book_list})
    return render_to_response("book_list.html", c)
def book_add(request):
    author = []
    flag = 0
    if request.POST:
        post = request.POST
        new_book = Book(
            ISBN = post["ISBN"],
            Title = post["Title"],
            AuthorID = post["AuthorID"],
            Publisher = post["Publisher"],
            PublishDate = post["PublishDate"],
            Price = post["Price"])  
        new_book.save()
        flag = 1
        author = Author.objects.filter(AuthorID = post["AuthorID"])
    if len(author)==0 and flag==1:
        return render_to_response("add_author.html")
    else:
        return render_to_response("add_book.html")
def author_add(request):
    if request.POST:
        post = request.POST
        new_author = Author(
            AuthorID = post["AuthorID"],
            Name = post["Name"],
            Age = post["Age"],
            Country = post["Country"])
        new_author.save()
    return render_to_response("add_author.html")
def book_find(request):
    findauthor = request.POST["findauthor"]
    author_found = Author.objects.filter(Name = findauthor)
    if len(author_found)!=0:
        for author in author_found:
           book_found = Book.objects.filter(AuthorID = author.AuthorID)
        c = Context({"book_list":book_found})
        return render_to_response("book_find.html",c)
    else:
        return render_to_response("sorry.html")
def return_find(request):
    return render_to_response("find.html")
def delete_book(request):
    id_=request.GET["id"]
    id2=Book.objects.get(id=id_)
    id2.delete()
    book_list=Book.objects.all()
    c=Context({"book_list":book_list})
    return render_to_response("book_list.html",c)
def show_book(request):
    id_=request.GET["id"]
    show=Book.objects.get(id = id_)
    author=Author.objects.get(AuthorID = show.AuthorID)
    c=Context({"show_book":show,"author":author})
    return render_to_response("show_book.html",c)
def change_book(request):
    id_=request.GET["id"]
    id2=Book.objects.get(id=id_)
    author=Author.objects.get(AuthorID = id2.AuthorID)
    if request.POST:
        post = request.POST
        id2.Publisher = post["Publisher"]
        id2.PublishDate = post["PublishDate"]
        id2.Price = post["Price"] 
        author.AuthorID = post["AuthorID"]
        author.Name = post["Name"]
        author.Age = post["Age"]
        author.Country = post["Country"]
        id2.save()
        author.save()
    c = Context({"id2":id2,"author":author})
    return render_to_response("change_book.html",c)
    