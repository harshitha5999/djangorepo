from django.shortcuts import render,redirect
from .forms import BookForms, ModelBookForms,SearchForm#CustomForms
from catalog.models import Book
from django.contrib import messages
#from django.utils import timezone

# Create your views here.

def form_view(request):
    msg=''
    if request.method =='POST':
        form = BookForms(request.POST)
        if form.is_valid():
            # book = Book(
            #     name=form.cleaned_data.get('name'),
            #     purchase_date=form.cleaned_data.get('pur_date'),
            #     genre=form.cleaned_data.get('genre'),
            #     author=form.cleaned_data.get('author')
            # )
            book = Book.objects.create(
                name=form.cleaned_data.get('name'),
                purchase_date=form.cleaned_data.get('purchase_date'),
                genre=form.cleaned_data.get('genre'),
                book_author=form.cleaned_data.get('book_author')
            )
            book.save()
            msg = 'Book Added Successfully!!!'
        else:
            msg = form.errors
    else:
        form = BookForms()
    return render(request,'form.html',{"msg":msg,"forms":form})

def model_form(request):
    msg=''
    if request.method =='POST':
        form = ModelBookForms(request.POST)
        if form.is_valid():
            form.save()
            msg = 'Book Added Successfully!!!'
        else:
            msg = form.errors
    else:
        form = ModelBookForms()
    return render(request,'form.html',{"msg":msg,"forms":form})

def html_form(request):
    value=''
    if request.method=='POST':
        value=request.POST.get('name')
        return render(request,'values.html',{'value':value})
    else:
        value = 'Wrong input'
    return render(request,'design.html')

def booksearch(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            q = form.cleaned_data.get('q')
            # book = Book.objects.filter(namw__contains=q,purchase_date_lte=timezone.now)
            book = Book.objects.filter(name__contains=q)
            form = None
            return render(request,'showtables.html',{'book':book,'form':form})
    else:
        form = SearchForm()
        b = Book.objects.all()
    return render(request,'showtables.html',{'book':b,'form':form})

def deletebook(request,id):
    book = Book.objects.get(id=id)
    book.delete()
    messages.success(request,'Deleted '+str(id)+' Successfully')
    return redirect('/')

def editbook(request,id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        form = ModelBookForms(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Book updated Successfully')
            return redirect('/')
    else:
        form=ModelBookForms(instance=book)
    return render(request,'editbook.html',{'form':form})