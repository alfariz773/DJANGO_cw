from django.shortcuts import render,redirect
from .models import local
from .forms import shelf
from django.core.paginator import Paginator

def home(request):
    books = local.objects.all().order_by('id')
    paginator = Paginator(books,5)
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'bookapp/home.html', {'page_obj': page_obj})

    
def add(request):
    if request.method == 'POST':
        form = shelf(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = shelf()
    return render(request, 'bookapp/add_book.html', {'form': form})    

def edit(request,pk):
    book = local.objects.get(pk=pk)
    if request.method == 'POST':
        form = shelf(request.POST,instance=book)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form= shelf(instance=book)
    return render(request, 'bookapp/edit.html', {'form': form})  

def delete(request, pk):
    book = local.objects.get(pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('home')
    return render(request, 'bookapp/delete.html', {'book': book})  


            

