from django.shortcuts import render
from .forms import bookForm
from .models import Booklet
def book_details(request):
    if request.method == 'POST':
        form = bookForm(request.POST)
        if form.is_valid():
            cust = form.save()
            book= Booklet.objects.all()
            return render(request,'data.html',{
               'books':book,
               'message': 'Your saved book:'})
    else:
        form =bookForm()
    return render(request,'index.html',{'form':form})